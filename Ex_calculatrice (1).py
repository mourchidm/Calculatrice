import tkinter as tk
import math

class Calculatrice(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.nombre1=""
        self.nombre2=""
        self.symbole_operation=""
        self.resultat=""
        self.sous_methode=False
        self.historique=[]
        self.position_historique=0
        self.creation_label()
        self.creation_button_chiffre()
        self.creation_button_operation()
        self.creation_button_autres()
        self.eval('tk::PlaceWindow . center')
        self.title('Calculatrice')

    def creation_label(self):
        titre=tk.Label(self, text='CALCULATRICE', font=('BOLD', 14), height=2)
        titre.grid(row=0, column=1, columnspan=5)
        self.calcul=tk.Label(self, text="", bg='white', font=1, width=22, height=2, relief='groove', borderwidth=4)
        self.calcul.grid(row=5, column=1, columnspan=5)
        label_hist = tk.Label(self, text="Précédent : ")
        label_hist.grid(row=1, column=1, columnspan=2)
        self.label_historique=tk.Label(self, text="", bg='white', font=1, width=22, relief='groove', borderwidth=4)
        self.label_historique.grid(row=2, column=1, columnspan=5)
        tk.Label(self,text="").grid(row=1, column=1, columnspan=5)
        tk.Label(self,text="").grid(row=4, column=1, columnspan=5)
        tk.Label(self,text="").grid(row=6, column=1, columnspan=5)
        tk.Label(self,text="").grid(row=12, column=1, columnspan=5)
        tk.Label(self,text="", height=1).grid(row=14, column=1, columnspan=5)
        tk.Label(self,text="", width=2).grid(row=0, column=0, rowspan=15)
        tk.Label(self,text="", width=2).grid(row=0, column=6, rowspan=15)

    def creation_button_chiffre(self):
        un=tk.Button(self, text='1', command=lambda : self.nombre('1'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        un.grid(row=7, column=1)
        deux=tk.Button(self, text='2', command=lambda :self.nombre('2'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        deux.grid(row=7, column=2)
        trois=tk.Button(self, text='3', command=lambda :self.nombre('3'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        trois.grid(row=7, column=3)
        quatre=tk.Button(self, text='4', command=lambda :self.nombre('4'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        quatre.grid(row=8, column=1)
        cinq=tk.Button(self, text='5', command=lambda :self.nombre('5'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        cinq.grid(row=8, column=2)
        six=tk.Button(self, text='6', command=lambda :self.nombre('6'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        six.grid(row=8, column=3)
        sept=tk.Button(self, text='7', command=lambda :self.nombre('7'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        sept.grid(row=9, column=1)
        huit=tk.Button(self, text='8', command=lambda :self.nombre('8'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        huit.grid(row=9, column=2)
        neuf=tk.Button(self, text='9', command=lambda :self.nombre('9'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        neuf.grid(row=9, column=3)
        zero=tk.Button(self, text='0', command=lambda :self.nombre('0'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove')
        zero.grid(row=10, column=1)
        virgule=tk.Button(self, text='.', command=lambda :self.nombre('.'), bg='darksalmon', fg='white', font=2, width=6, height=1,borderwidth=5, relief='groove')
        virgule.grid(row=10, column=2, columnspan=2)
        pi=tk.Button(self, text='𝝅', command=lambda : self.nombre('pi'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        pi.grid(row=10, column=5)

    def nombre(self, chiffre):
        if self.resultat!="" :
            self.label_historique.config(text=self.nombre1 + self.symbole_operation + self.nombre2 + ' = ' + str(self.resultat))
            self.position_historique = 0
            self.supprimer()
        if self.sous_methode==False:
            if chiffre=='pi' and self.symbole_operation=="" :
                self.nombre1='𝝅'
            elif chiffre=='pi' and self.symbole_operation!="" :
                self.nombre2='𝝅'
            elif chiffre=='²' and self.symbole_operation=="":
                if self.nombre1!="":
                    self.nombre1=self.nombre1+chiffre
                    self.sous_methode=True
            elif chiffre=='²' and self.symbole_operation!="":
                if self.nombre2!="":
                    self.nombre2=self.nombre2+chiffre
                    self.sous_methode=True
            elif (chiffre=='cos' or chiffre=='sin' or chiffre=='tan' or chiffre=='√') and self.symbole_operation=="" :
                if self.nombre1!="":
                    self.nombre1=chiffre+'('+self.nombre1+')'
                    self.sous_methode=True
            elif (chiffre=='cos' or chiffre=='sin' or chiffre=='tan' or chiffre=='√') and self.symbole_operation!="" :
                if self.nombre2!="":
                    self.nombre2=chiffre+'('+self.nombre2+')'
                    self.sous_methode=True
            elif chiffre=='.' and self.symbole_operation=="" and self.nombre1=="":
                self.nombre1='0.'
            elif chiffre=='.' and self.symbole_operation!="" and self.nombre2=="":
                self.nombre2='0.'
            elif self.symbole_operation=="" :
                self.nombre1=self.nombre1+chiffre
            elif self.symbole_operation != "" :
                self.nombre2=self.nombre2+chiffre
            self.calcul.config(text=self.nombre1+self.symbole_operation+self.nombre2, width=0)

    def creation_button_operation(self):
        plus=tk.Button(self, text='+', command=lambda : self.operation('+'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        plus.grid(row=7, column=4)
        moins = tk.Button(self, text='-', command=lambda : self.operation('-'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        moins.grid(row=8, column=4)
        multiplier = tk.Button(self, text='*', command=lambda : self.operation('*'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        multiplier.grid(row=9, column=4)
        diviser = tk.Button(self, text='/', command=lambda : self.operation('/'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        diviser.grid(row=10, column=4)
        racine = tk.Button(self, text='√x', command=lambda: self.nombre('√'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        racine.grid(row=11, column=4)
        cosinus=tk.Button(self, text='cos', command=lambda : self.nombre('cos'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        cosinus.grid(row=7, column=5)
        sinus=tk.Button(self, text='sin', command=lambda : self.nombre('sin'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        sinus.grid(row=8, column=5)
        tang = tk.Button(self, text='tan', command=lambda: self.nombre('tan'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        tang.grid(row=9, column=5)
        carre=tk.Button(self, text="x²", command= lambda: self.nombre('²'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove')
        carre.grid(row=11, column=5)
        egal = tk.Button(self, text='Entrer', command= self.calculer, bg='darkred', fg='white', font=2, width=11, height=1,borderwidth=5, relief='groove')
        egal.grid(row=11, column=1, columnspan=3)

    def operation(self, symbole):
        if self.resultat!="" :
            self.label_historique.config(text=self.nombre1 + self.symbole_operation + self.nombre2 + ' = ' + str(self.resultat), width=0)
            self.position_historique = 0
            self.supprimer()
        if self.nombre1=="" :
            if self.historique!=[] :
                self.nombre1=self.historique[len(self.historique)-1][4]
            else :
                self.nombre1='0'
        self.symbole_operation=symbole
        self.sous_methode = False
        self.calcul.config(text=self.nombre1+self.symbole_operation+self.nombre2, width=0)

    def calculer(self):
        n1=self.nombre1
        n2=self.nombre2
        if '𝝅' in n1 :
            n1=n1.replace('𝝅',str(math.pi) )
        if '𝝅' in n2 :
            n2= n2.replace('𝝅', str(math.pi))
        if '²' in n1 :
            n1=str(float(n1[:len(n1)-1])**2)
        if '²' in n2 :
            n2=str(float(n2[:len(n2)-1])**2)
        if 'tan' in n1 :
            n1=str(math.tan(float(n1[4:len(n1)-1])))
        if 'tan' in n2 :
            n2=str(math.tan(float(n2[4:len(n2)-1])))
        if 'cos' in n1 :
            n1=str(math.cos(float(n1[4:len(n1)-1])))
            print(n1)
        if 'cos' in n2 :
            n2=str(math.cos(float(n2[4:len(n2)-1])))
        if 'sin' in n1 :
            n1=str(math.sin(float(n1[4:len(n1)-1])))
        if 'sin' in n2 :
            n2=str(math.sin(float(n2[4:len(n2)-1])))
        if '√' in n1 :
            n1=str(math.sqrt(float(n1[2:len(n1)-1])))
        if '√' in n2 :
            n2=str(math.sqrt(float(n2[2:len(n2)-1])))
        if self.symbole_operation=='+' :
            self.resultat=float(n1)+float(n2)
        elif self.symbole_operation=='-':
            self.resultat=float(n1)-float(n2)
        elif self.symbole_operation=='*':
            self.resultat=float(n1)*float(n2)
        elif self.symbole_operation=='/':
            self.resultat=float(n1)/float(n2)
        self.calcul.config(text=self.nombre1+self.symbole_operation+self.nombre2+' = '+str(self.resultat), width=0)
        if self.nombre1=="" and self.nombre2=="":
            self.calcul.config(text="", width=22)
        elif self.nombre2=="" :
            self.resultat = float(n1)
            self.calcul.config(text=self.nombre1 + ' = ' + str(self.resultat), width=0)
        self.historique.append([self.nombre1, self.symbole_operation, self.nombre2,' = ', str(self.resultat)])

    def creation_button_autres(self):
        clear = tk.Button(self, text='Vider', command=self.supprimer, bg='dimgray', fg='white', font=2, width=11, borderwidth=2, relief='groove')
        clear.grid(row=13, column=1, columnspan=3)
        quitter = tk.Button(self, text='Quitter', command=self.destroy, bg='dimgray', fg='white', font=2, width=8, borderwidth=2, relief='groove')
        quitter.grid(row=13, column=4, columnspan=2)
        fleche_up=tk.Button(self, text='↑', command=lambda:self.fleche('up'), bg='dimgray', fg='white', font=2, width=2, borderwidth=2, relief='groove')
        fleche_up.grid(row=3, column=1)
        fleche_down = tk.Button(self, text='↓', command=lambda: self.fleche('down'), bg='dimgray', fg='white', font=2, width=2, borderwidth=2, relief='groove')
        fleche_down.grid(row=3, column=2)
        repeter=tk.Button(self, text='Répéter', command=self.relancer, bg='dimgray', fg='white', font=2, width=12, borderwidth=2, relief='groove')
        repeter.grid(row=3, column=3, columnspan=3)

    def supprimer(self):
        if self.resultat!="":
            self.label_historique.config(text=self.nombre1+self.symbole_operation+self.nombre2+' = '+str(self.resultat), width=0)
        self.nombre1=""
        self.nombre2=""
        self.symbole_operation=""
        self.resultat=""
        self.calcul.config(text="", width=22)
        self.sous_methode=False

    def fleche(self, sens):
        chaine=""
        if sens=='up' :
            self.position_historique += 1
            for element in self.historique[len(self.historique)-2-self.position_historique] :
                chaine+=element
            self.label_historique.config(text=chaine, width=0)
        else :
            self.position_historique -= 1
            for element in self.historique[len(self.historique)-2-self.position_historique] :
                chaine+=element
            self.label_historique.config(text=chaine, width=0)

    def relancer(self):
        self.nombre1=self.historique[len(self.historique)-2-self.position_historique][0]
        self.nombre2=self.historique[len(self.historique)-2-self.position_historique][2]
        self.symbole_operation=self.historique[len(self.historique)-2-self.position_historique][1]
        self.calculer()

def main():
    f=Calculatrice()
    f.mainloop()

main()