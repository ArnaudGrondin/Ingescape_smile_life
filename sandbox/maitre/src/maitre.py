#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

import random
import ingescape as igs


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Maitre(metaclass=Singleton):
    def __init__(self):
        # Gestion du jeu
        self.nb_joueurs = 0
        self.cartes = []
        self.pioche = []
        self.defausse = []
        self.tour = 0
        self.joueurs = []
        self.whiteboard = None

    def initialiser_jeu(self, nb_joueurs, cartes_disponibles):
        """
        Initialise la partie avec le nombre de joueurs et les cartes disponibles.
        Mélange les cartes pour former la pioche.
        Réinitialise les attributs de la partie, comme la défausse et le tour.

        """
        self.nb_joueurs = nb_joueurs
        self.cartes = cartes_disponibles
        random.shuffle(self.cartes)
        self.pioche = self.cartes[:]
        self.defausse = []
        self.tour = 0

        igs.info(f"Jeu initialisé avec {self.nb_joueurs} joueurs et {len(self.cartes)} cartes.")

    def distribuer_cartes(self):
        """
        Distribue 5 cartes à chaque joueur au début de la partie.
        Appelle le service setHand sur chaque agent joueur pour leur envoyer leurs cartes.
        """
        if not self.joueurs:
            raise ValueError("Aucun joueur connecté.")

        for joueur in self.joueurs:
            joueur_cartes = [self.pioche.pop() for _ in range(5)]
            igs.service_call(joueur, "setHand", (joueur_cartes,), "")
            igs.info(f"Cartes distribuées au joueur {joueur}: {joueur_cartes}")

    def joueur_suivant(self):
        """
        Passe au joueur dans la liste self.joueurs.
        Appelle le service yourTurn sur l'agent joueur concerné.
        """
        self.tour = (self.tour + 1) % self.nb_joueurs
        joueur_actuel = self.joueurs[self.tour]
        igs.service_call(joueur_actuel, "yourTurn", (), "")
        igs.info(f"C'est au tour du joueur {joueur_actuel}.")

    def mettre_a_jour_whiteboard(self):
        """
        Met à jour l'état du jeu (pioche restante et carte sur la défausse) sur le tableau blanc.
        Appelle le service updateGameState sur l'agent whiteboard.
        """
        pioche_restante = len(self.pioche)
        defausse_top = self.defausse[-1] if self.defausse else "Vide"
        igs.service_call(self.whiteboard, "updateGameState", (pioche_restante, defausse_top), "")
        igs.info("État du jeu mis à jour sur le whiteboard.")

    def jouer_carte(self, joueur, carte):
        """
        Appelé lorsque le joueur défausse une carte
        Met à jour le tableau blanc pour refléter l'action
        """
        self.defausse.append(carte)
        igs.info(f"Joueur {joueur} a joué la carte {carte}.")
        self.mettre_a_jour_whiteboard()

    def piocher_carte(self, joueur):
        """
        Donne une carte au joueur depuis la pioche.
        Si la pioche est vide, un message d'erreur est enregistré.
        """
        if not self.pioche:
            igs.error("Pioche vide.")
            return None

        carte = self.pioche.pop()
        igs.service_call(joueur, "addCard", (carte,), "")
        igs.info(f"Joueur {joueur} a pioché la carte {carte}.")
        self.mettre_a_jour_whiteboard()

    def calculer_scores(self):
        """
        Calcule et affiche les scores à la fin de la partie.
        Demande à chaque joueur son score via le service getScore
        Détermine le gagnant et affiche les scores sur le tableau blanc.
        """
        scores = {}
        for joueur in self.joueurs:
            score = igs.service_call(joueur, "getScore", (), "score")
            scores[joueur] = score

        gagnant = max(scores, key=scores.get)
        igs.info(f"Partie terminée. Scores : {scores}. Gagnant : {gagnant}.")
        igs.service_call(self.whiteboard, "showScores", (scores,), "")



