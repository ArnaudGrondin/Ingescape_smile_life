#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Whiteboard.py
#  Whiteboard
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


class Whiteboard(metaclass=Singleton):
    def __init__(self):
        # inputs
        self.TitleI = "Smile Life Game"
        self.BackgroundcolorI = "white"
        self.LabelsvisibleI = True
        self.ChatmessageI = []
        self.Ui_CommandI = None

        self.game_state = {"pioche": 0, "defausse_top": "Vide"}

        # outputs
        self._LastchatmessageO = None
        self._LastactionO = None
        self._Ui_ErrorO = None
        self.scores = {}

    # outputs
    @property
    def LastchatmessageO(self):
        return self._LastchatmessageO

    @LastchatmessageO.setter
    def LastchatmessageO(self, value):
        self._LastchatmessageO = value
        if self._LastchatmessageO is not None:
            igs.output_set_string("lastChatMessage", self._LastchatmessageO)
    @property
    def LastactionO(self):
        return self._LastactionO

    @LastactionO.setter
    def LastactionO(self, value):
        self._LastactionO = value
        if self._LastactionO is not None:
            igs.output_set_string("lastAction", self._LastactionO)
    @property
    def Ui_ErrorO(self):
        return self._Ui_ErrorO

    @Ui_ErrorO.setter
    def Ui_ErrorO(self, value):
        self._Ui_ErrorO = value
        if self._Ui_ErrorO is not None:
            igs.output_set_string("ui_error", self._Ui_ErrorO)

    # services

    def update_game_state(self, pioche_restante, defausse_top):
        """
        Met à jour l'état du jeu avec les informations sur la pioche et la défausse.
        """
        self.game_state["pioche"] = pioche_restante
        self.game_state["defausse_top"] = defausse_top
        igs.info(f"État du jeu mis à jour : Pioche restante = {pioche_restante}, Défausse top = {defausse_top}.")

    def show_scores(self, scores):
        """
        Affiche les scores des joueurs.
        """
        self.scores = scores
        scores_message = "\n".join([f"{joueur}: {score} points" for joueur, score in scores.items()])
        igs.info(f"Scores affichés :\n{scores_message}")
        self.add_text(f"Scores :\n{scores_message}", 10, 50, "black")

    def Chat(self, sender_agent_name, sender_agent_uuid, Message):
        pass
        # add code here if needed

    def Snapshot(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed

    def Clear(self, sender_agent_name, sender_agent_uuid):
        """
        Réinitialise le tableau blanc.
        """
        igs.service_call("Whiteboard", "clear", (), "")
        igs.info("Tableau blanc réinitialisé.")

    def Showlabels(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed

    def Hidelabels(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed

    def Addshape(self, sender_agent_name, sender_agent_uuid, Type, X, Y, Width, Height, Fill, Stroke, Strokewidth):
        pass
        # add code here if needed

    def Addtext(self, sender_agent_name, sender_agent_uuid, Text, X, Y, Color):
        """
        Affiche un texte sur le tableau blanc.
        """
        igs.service_call("Whiteboard", "addText", (text, x, y, color), "")
        igs.info(f"Texte ajouté au tableau : '{text}' à la position ({x}, {y}) avec la couleur {color}.")

    def Addimage(self, sender_agent_name, sender_agent_uuid, Base64, X, Y, Width, Height):
        pass
        # add code here if needed

    def Addimagefromurl(self, sender_agent_name, sender_agent_uuid, Url, X, Y):
        pass
        # add code here if needed

    def Remove(self, sender_agent_name, sender_agent_uuid, Elementid):
        pass
        # add code here if needed

    def Translate(self, sender_agent_name, sender_agent_uuid, Elementid, Dx, Dy):
        pass
        # add code here if needed

    def Moveto(self, sender_agent_name, sender_agent_uuid, Elementid, X, Y):
        pass
        # add code here if needed

    def Setstringproperty(self, sender_agent_name, sender_agent_uuid, Elementid, Property, Value):
        pass
        # add code here if needed

    def Setdoubleproperty(self, sender_agent_name, sender_agent_uuid, Elementid, Property, Value):
        pass
        # add code here if needed

    def Getelementids(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed

    def Getelements(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed


