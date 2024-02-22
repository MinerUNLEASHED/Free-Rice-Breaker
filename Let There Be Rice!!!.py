import time
import pyautogui
import random
import win32clipboard

def moving_cursor(x, y):
    # time_to_travel = random.random()
    pyautogui.moveTo(x, y, 0, pyautogui.easeInQuad)

def return_last_copy():
    win32clipboard.OpenClipboard()
    last_copy = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return last_copy

def select_text(x,y):
    moving_cursor(x,y)
    pyautogui.drag(400, 0, 0.3, button='left')
    pyautogui.hotkey('ctrl', 'c')
    return_copy = return_last_copy()
    return return_copy

while True:
    for i in range(random.randint(1,30)):
        clicked = False
        time.sleep(1.5)
        question_text = select_text(525,202)
        question_text = question_text.replace('x', '*')
        try:
            question_answer = eval(question_text)
        except:
            pass

        first_answer_text = select_text(525,270)
        try:
            if question_answer == eval(first_answer_text):
                pyautogui.click(587, 276)
                clicked = True
        except:
            pass

        second_answer_text = select_text(525,319)
        try:
            if question_answer == eval(second_answer_text):
                pyautogui.click(599, 319)
                clicked = True
        except:
            pass

        third_answer_text = select_text(525,376)
        try:
            if question_answer == eval(third_answer_text):
                pyautogui.click(601, 378)
                clicked = True
        except:
            pass

        fourth_answer_text = select_text(528,443)
        try:
            if question_answer == eval(fourth_answer_text):
                pyautogui.click(602, 426)
                clicked = True
        except:
            pass
        print(question_text, first_answer_text, second_answer_text, third_answer_text, fourth_answer_text)
        if clicked == False:
            try:
                if question_answer == eval(first_answer_text):
                    pyautogui.click(587,276)
                elif question_answer == eval(second_answer_text):
                    pyautogui.click(599,319)
                elif question_answer == eval(third_answer_text):
                    pyautogui.click(601,378)
                elif question_answer == eval(fourth_answer_text):
                    pyautogui.click(602,426)
                else:
                    pass
            except:
                pass


        # print(pyautogui.size())
    pyautogui.click(89,50)
    time.sleep(3)