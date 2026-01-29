class combat:

    def PlayCardoFight(self, Ryan, CardoChef):

        while True:
            if self.GetAttackResult(Ryan, CardoChef) == "Rip poto tu as perdu ton cardo":
                print("Rip poto tu as perdu ton cardo")
                break

            if self.GetAttackResult(CardoChef, Ryan) == "Rip il a voler ton cardo":
                print("Rip il a voler ton cardo")
                break

            @staticmethod
            def GetAttackResult(CombattantA, CombattantB):

                CombattantAATKMontant = CombattantA.Attack()

                CombattantBblockMontant = CombattantB.Block()

                Dammage2CombattantB = math.ceil(CombattantAATKMontant - CombattantBblockMontant)

                CombattantB.health = CombattantB.health - dammage2CombattantB

                print("{} {} {}".format(CombattantA.prenom, CombattantB.prenom, damage2CombattantB))

                print("{} {} {}".format(CombbatantB.prenom, CombattantB.health))

                if CombattantB.health <= 0:

                    print("{} est mort a cause de {} mais il a gagner".format(CombattantB.prenom, CombattantA.prenom))

                    return "Rip Poto tu as perdu ton cardo"
                else:
                    return "reviens prendre un cardo"
