# author: Fatemeh Talebi
# error handling class
class My_Exception_Handling(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Error: {self.message}"


# -------------------------------------------------------
class PlayerSelection:

    def __init__(self, code, age, height, weight):
        self.code = code
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.code} {self.age} {self.height} {self.weight}"

    def weight_validation(self):
        PlayerSelection.check_integer(self.age,"age has invalid type")
        PlayerSelection.check_float(self.weight,"weight has invalid type")
        age=int(self.age)
        weight=float(self.weight)
        if age >= 15 and age <= 35:  # check range of age
            if age >= 15 and age < 25:  # check range of weight based on age
                if weight >= 60 and weight < 80:
                    return True
                else:
                    raise My_Exception_Handling(
                        "weight out of range.this oerson is not allowed to register"
                    )

            if age >= 25 and age < 35:  # check range of weight based on age
                if weight >= 50 and weight < 75:
                    return True
                else:
                    raise My_Exception_Handling(
                        "weight out of range.this person is not allowed to register"
                    )
        else:
            raise My_Exception_Handling(
                "age out of range. this person is not allowed to register"
            )

    def height_validation(self):
        PlayerSelection.check_integer(self.height,"height has invalid type.")
        height=int(self.height)
        if not ( height >= 170 and height <= 190 ):
            raise My_Exception_Handling(
                "height is out of range.this person is not allowed to register"
            )

    @staticmethod
    def check_integer(number, message):
        try:
            int(number)
            
        except:
            raise My_Exception_Handling(message)

    @staticmethod
    def check_float(number,message):
        try:
            float(number)
        except:
            raise My_Exception_Handling(message)

    @classmethod
    def player_register(cls, player):
        try:
            player.weight_validation()
            player.height_validation()
            print("player registered successfully!")
            return (player.code, player.age, player.height, player.weight)
        except My_Exception_Handling as error:
            raise My_Exception_Handling(error.message)


# ----------------------
# main app
myList = []

while True:
    try:
        code = int(input("enter code:"))
        if code == 0:  # break if user enter 0
            break
        age = input("enter age:")
        height = input("enter height:")
        weight = input("enter weight:")
        selection = PlayerSelection(code, age, height, weight)
        PlayerSelection.player_register(selection)
        dict = {"code": code, "age": age, "height": height, "weight": weight}
        myList.append(dict)

    except My_Exception_Handling as error:
        print(error)


for player in myList:  # print validate players list
    print(player)
