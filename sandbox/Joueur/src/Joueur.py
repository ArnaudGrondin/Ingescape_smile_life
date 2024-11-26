#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Joueur.py
#  Joueur
#  Created by Ingenuity i/o on 2024/11/22
#
# "no description"
#
import ingescape as igs


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Joueur(metaclass=Singleton):
    def __init__(self):
        self.main = []  # Liste des cartes en main
        self.whiteboard = None  # Référence au tableau blanc
        self.maitre = None  # Référence au maître
        self.score = 0  # Score du joueur

    def set_hand(self, cartes):
        """
        Initialise les cartes en main du joueur.
        """
        self.main = cartes
        igs.info(f"Main initialisée : {self.main}")

    def ajouter_carte(self, carte):
        """
        Ajoute une carte à la main du joueur.
        """
        self.main.append(carte)
        igs.info(f"Carte ajoutée à la main : {carte}")

    def jouer_carte(self, carte_index):
        """
        Joue une carte de la main et l'envoie au maître.
        """
        if carte_index < 0 or carte_index >= len(self.main):
            igs.error("Index de carte invalide.")
            return

        carte = self.main.pop(carte_index)
        igs.service_call(self.maitre, "jouerCarte", (igs.agent_name(), carte), "")
        igs.info(f"Carte jouée : {carte}")

    def piocher_carte(self):
        """
        Demande au maître de piocher une carte.
        """
        igs.service_call(self.maitre, "piocherCarte", (igs.agent_name(),), "")
        igs.info("Demande de pioche envoyée au maître.")

    def calculer_score(self):
        """
        Calcule le score du joueur en fonction des cartes jouées.
        """
        self.score = sum(int(carte.split("_")[1]) for carte in self.main if "_" in carte)
        return self.score

    def notifier_tour(self):
        """
        Notification indiquant que c'est au tour du joueur.
        """
        igs.info("C'est votre tour de jouer.")
        # Simuler une action du joueur
        if len(self.main) > 0:
            self.jouer_carte(0)  # Joue la première carte
        else:
            self.piocher_carte()  # Pioche si aucune carte à jouer
        igs.service_call(self.maitre, "finTour", (igs.agent_name(),), "")

    def afficher_main(self):
        """
        Affiche les cartes en main sur le whiteboard.
        """
        if self.whiteboard:
            cartes_str = ", ".join(self.main)
            igs.service_call(self.whiteboard, "addText", (cartes_str, 10, 10, "blue"), "")


