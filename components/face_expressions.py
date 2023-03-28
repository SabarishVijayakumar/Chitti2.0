##################################################
# AUTHOR                                         #
# Krushna kumar V                                #
##################################################


from adafruit_servokit import ServoKit
from components.servo_worker import Servo_Worker


#Mouth full close 65
#Mouse full open 90
#left eye 97 right eye 83
#to move left eyebrow down decrease angle.
#to move right eyebrow down increase angle.
#always increase/decrease in count of  5
#eye left side 97 and right side 83

#Class to set expressions to face using servo motors
_LEFT_EYE = 7
_RIGHT_EYE = 14
_LEFT_EYE_BROW = 11
_RIGHT_EYE_BROW = 12
_MOUTH = 15

#Angle macro
_SMILE_LEFT_EYE = 90
_SMILE_RIGHT_EYE = 90
_SMILE_LEFT_EYE_BROW = 95
_SMILE_RIGHT_EYE_BROW = 85
_SMILE_MOUTH = 80

_SAD_LEFT_EYE = 90
_SAD_RIGHT_EYE = 83
_SAD_LEFT_EYE_BROW = 90
_SAD_RIGHT_EYE_BROW = 90
_SAD_MOUTH = 65

_ANGRY_LEFT_EYE = 90
_ANGRY_RIGHT_EYE = 97
_ANGRY_LEFT_EYE_BROW = 110
_ANGRY_RIGHT_EYE_BROW = 70
_ANGRY_MOUTH = 65

_DEFAULT_LEFT_EYE = 90
_DEFAULT_RIGHT_EYE = 90
_DEFAULT_LEFT_EYE_BROW = 98
_DEFAULT_RIGHT_EYE_BROW = 82
_DEFAULT_MOUTH = 65



class Face_Expressions:
   
  
    def __init__(self):
        self.lefteye = Servo_Worker(_LEFT_EYE)
        self.righteye = Servo_Worker(_RIGHT_EYE)
        self.mouth = Servo_Worker(_MOUTH)
        self.lefteye_brow = Servo_Worker(_LEFT_EYE_BROW)
        self.righteye_brow = Servo_Worker(_RIGHT_EYE_BROW)       
        self.set_expression_default()     
        

    def set_expression_smile(self):
        #self.lefteye.set_angle(_SMILE_LEFT_EYE)
        self.righteye.set_angle(_SMILE_RIGHT_EYE)
        self.mouth.set_angle(_SMILE_MOUTH)
        self.lefteye_brow.set_angle(_SMILE_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_SMILE_RIGHT_EYE_BROW)
            
    
    def set_expression_sad(self):
        #self.lefteye.set_angle(_SAD_LEFT_EYE)
        self.righteye.set_angle(_SAD_RIGHT_EYE)
        self.mouth.set_angle(_SAD_MOUTH)
        self.lefteye_brow.set_angle(_SAD_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_SAD_RIGHT_EYE_BROW)
        
    def set_expression_angry(self):
        #self.lefteye.set_angle(_ANGRY_LEFT_EYE)
        self.righteye.set_angle(_ANGRY_RIGHT_EYE)
        self.mouth.set_angle(_ANGRY_MOUTH)
        self.lefteye_brow.set_angle(_ANGRY_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_ANGRY_RIGHT_EYE_BROW)

    def set_expression_default(self):
        #self.lefteye.set_angle(_DEFAULT_LEFT_EYE)
        self.righteye.set_angle(_DEFAULT_RIGHT_EYE)
        self.mouth.set_angle(_DEFAULT_MOUTH)
        self.lefteye_brow.set_angle(_DEFAULT_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_DEFAULT_RIGHT_EYE_BROW)
    
    
