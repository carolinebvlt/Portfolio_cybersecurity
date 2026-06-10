# Check and evaluate the stregth of a password

import re


def check_password_strength(password_param) :

    # Score init
    score = 0

    # Lenght check ( >= 8 -> 1 point, >= 12 -> 2 points)
    password_length = len(password_param)
    if password_length >= 12 :
        score += 2
    elif password_length >= 8 : 
        score += 1

    # Capitalized check (if at least 1 -> 1 point)
    capitalized = re.findall("[A-Z]", password_param)
    if len(capitalized) >= 1 :
        score += 1

    # number check (if at least 1 -> 1 point)
    digits = re.findall("\d", password_param)
    if len(digits) >= 1 :
        score += 1

    # Special char check
    special_chars = re.findall("[^a-zA-Z0-9]", password_param)
    if len(special_chars) >= 1 :
        score += 1

    # return the final note and the strength level
    strength_level = None
    if score == 5 :
        strength_level = "High"
    elif score >= 3 :
        strength_level = "Medium"
    else :
        strength_level = "Low"
    
    # return the score and the level
    return score, strength_level