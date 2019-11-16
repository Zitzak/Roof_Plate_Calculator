from roof_plates import RoofPlates
import tkinter as tk
from app import App


if __name__ == '__main__':
    test = [[110, 130], [130, 150], [150, 170], [170, 190], [190, 210]]  ## <---------
    # test = [[130, 150], [150, 170], [170, 190], [190, 210], [210, 230], [230, 250]]  ## <---------
    # plates = RoofPlates()
    # size_roof = dict.fromkeys((item[0] for item in test), False)
    my_window = tk.Tk()
    my_window.title("Dak platen omrekenen")
    my_window.geometry("450x500")
    frame_a = App(my_window)
    frame_a.grid(row=0, column=0)
    # print(frame_a.size_plank)
    my_window.mainloop()



    # difference = abs(test[0][0] - test[0][1])
    # if difference == 10:
    # 	plates.make_vars(difference, size_roof)
    # elif difference == 20:
    # 	plates.make_vars(difference, size_roof)
    # else:
    # 	pass ##<-------- Invalid difference



    # plates.run()

    # print("FINAL")
    # plates.print_test_final()
