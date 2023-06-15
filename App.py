from tkinter import*
import tkinter as tk

# Khởi tạo danh sách phòng khách sạn
rooms = {
    "101": {"type": "đơn", "price": 100, "status": "trống"},
    "102": {"type": "đơn", "price": 120, "status": "đã đặt"},
    "103": {"type": "đôi", "price": 150, "status": "trống"},
    "104": {"type": "đôi", "price": 180, "status": "đã đặt"},
    "105": {"type": "suite", "price": 250, "status": "trống"},
    "106": {"type": "suite", "price": 300, "status": "trống"}
}
# Biến toàn cục lưu trữ tổng doanh thu
total_revenue = 0

# Hàm hiển thị danh sách phòng
def list_room():
    Danh_sach = tk.Toplevel()
    Danh_sach.title("Danh sách phòng")
    Danh_sach.geometry('400x400+450+120')
    dong1 = Label(Danh_sach,text='Danh sách phòng:', font='Times 17',height=4)
    dong1.pack()
    dong2 = Label(Danh_sach,text='',font='Times 15')
    dong2.pack()
    for room_num, room_info in rooms.items():
        dong2.config(text=dong2.cget("text") + f"Phòng {room_num} - Loại phòng: {room_info['type']}, Giá phòng: {room_info['price']}"+'\n')

# Hàm tìm kiếm phòng
def find_room():
    Tim_phong = tk.Toplevel()
    Tim_phong.title("Tìm phòng")
    Tim_phong.geometry('1000x600+450+120')
    dong1 = Label(Tim_phong,text='Tìm kiếm phòng', font='Times 17 bold',height=2)
    dong1.grid(row=0,columnspan=4)
    dong2 = Label(Tim_phong,text='Nhập loại phòng (đơn/đôi/suite): ', font='Times 15',height=1)
    dong2.grid(row=1,column=0)
    entroom = Entry(Tim_phong,font='Times 15',width=15)
    entroom.grid(row=1,column=1)
    entroom.focus()
    dong3 = Label(Tim_phong,text='Nhập khoảng giá (vd: 100-150): ', font='Times 15',height=3)
    dong3.grid(row=3,column=0)
    entprice = Entry(Tim_phong,font='Times 15',width=15)
    entprice.grid(row=3,column=1)
    dong4 = Label(Tim_phong,text='Nhập tình trạng phòng (đã đặt/trống): ', font='Times 15',height=1)
    dong4.grid(row=4,column=0)
    entstatus= Entry(Tim_phong,font='Times 15',width=15)
    entstatus.grid(row=4,column=1)
    def ketqua():
        label_ketqua = Label(Tim_phong,text='',font='Times 15')
        label_ketqua.grid(row=10, columnspan=2)
        room_type = entroom.get()
        price_range = entprice.get()
        room_status = entstatus.get()
        min_price, max_price = price_range.split("-") if "-" in price_range else (None, None)
        for room_num, room_info in rooms.items():
            if (not room_type or room_info["type"] == room_type) and \
                (not min_price or room_info["price"] >= int(min_price)) and \
                (not max_price or room_info["price"] <= int(max_price)) and \
                (not room_status or ("status" in room_info and room_info["status"] == room_status)):
                label_ketqua.config(text=label_ketqua.cget("text") + f"Phòng {room_num} - Loại phòng: {room_info['type']}, Giá phòng: {room_info['price']}"+'\n')
    tim_kiem = Button(Tim_phong,text='Tìm kiếm',font='Time 18',command=ketqua)
    tim_kiem.grid(row=6, column=3)
    dong5 = Label(Tim_phong, text='\n\n\n\n\nKết quả tìm kiếm: ', font='Times 15')
    dong5.grid(row=9, column=0)

# Hàm đặt phòng
def check_in():
    Dat_phong=tk.Toplevel()
    Dat_phong.title("Đặt phòng")
    Dat_phong.geometry('1000x600+450+120')
    dong1 = Label(Dat_phong,text='Đặt phòng', font='Times 17',height=4)
    dong1.grid(row=0,columnspan=3)
    dong2 = Label(Dat_phong,text='Nhập số phòng cần đặt: ', font='Times 15')
    dong2.grid(row=1,column=0)
    entroom = Entry(Dat_phong,font='Times 15')
    entroom.grid(row=1,column=1)
    entroom.focus()
    dong3 = Label(Dat_phong,text='Nhập số ngày ở: ', font='Times 15',height=3)
    dong3.grid(row=3,column=0)
    entday = Entry(Dat_phong,font='Times 15')
    entday.grid(row=3,column=1)
    def ketqua1():
        global total_revenue
        room_num = entroom.get()
        num_days = int(entday.get())
        label_ketqua = Label(Dat_phong,text='\t\t\t\t',font='Times 15')
        label_ketqua.grid(row=7,columnspan=1)
        if room_num in rooms:
            room_info = rooms[room_num]
            if room_info["status"] == "trống":
                total_price = room_info["price"] * num_days
                label_ketqua.config(text = label_ketqua.cget("text") + f"Đặt phòng thành công! Tổng giá trị đơn hàng là {total_price} đồng.")
                rooms[room_num]["status"] = "đã đặt"
                total_revenue += total_price
            else:
                label_ketqua.config(text=label_ketqua.cget("text") + "Phòng đã được đặt." '\n' "Vui lòng chọn một phòng khác hoặc thực hiện các thao tác đổi hoặc hủy phòng." )
        else:
            label_ketqua.config(text=label_ketqua.cget("text") + "Phòng không có sẵn hoặc không tồn tại.")
    enter = Button(Dat_phong,text='Đặt phòng',font='Time 15',command=ketqua1)
    enter.grid(row=4, column=1)
    dong4 = Label(Dat_phong,text='Kết quả: ',font='Times 15',height=5)
    dong4.grid(row=5,column=0)

# Hàm đổi phòng
def change_room():
    Doi_phong=tk.Toplevel()
    Doi_phong.title("Đổi phòng")
    Doi_phong.geometry('1000x600+450+120')
    dong1 = Label(Doi_phong,text='Đổi phòng', font='Times 17',height=4)
    dong1.grid(row=0,columnspan=3)
    dong2 = Label(Doi_phong,text='Nhập số phòng ban đầu: ', font='Times 15')
    dong2.grid(row=1,column=0)
    ent_room_old = Entry(Doi_phong,font='Times 15')
    ent_room_old.grid(row=1,column=1)
    ent_room_old.focus()
    dong3 = Label(Doi_phong,text='Nhập số phòng mới: ', font='Times 15',height=3)
    dong3.grid(row=2,column=0)
    ent_room_new = Entry(Doi_phong,font='Times 15')
    ent_room_new.grid(row=2,column=1)
    dong4 = Label(Doi_phong,text='Nhập số ngày ở: ', font='Times 15')
    dong4.grid(row=3,column=0)
    entday = Entry(Doi_phong,font='Times 15')
    entday.grid(row=3,column=1)
    def doi_phong():
        old_room_num = ent_room_old.get()
        new_room_num = ent_room_new.get()
        num_days = int(entday.get())
        label_ketqua = Label(Doi_phong,text='',font='Times 15')
        label_ketqua.grid(row=7,columnspan=1)
        
        if old_room_num in rooms and new_room_num in rooms:
            old_room_info = rooms[old_room_num]
            new_room_info = rooms[new_room_num]
            if not ("status" in old_room_info and old_room_info["status"] == "đã đặt"):
                label_ketqua.config(text = label_ketqua.cget("text") + "Phòng ban đầu chưa được đặt.")
            elif "status" in new_room_info and new_room_info["status"] == "đã đặt":
                label_ketqua.config(text = label_ketqua.cget("text") + "Phòng mới đã được đặt.")
            else:
                rooms[old_room_num]["status"] = "trống"
                rooms[new_room_num]["status"] = "đã đặt"
                label_ketqua.config(text = label_ketqua.cget("text") + f"Đổi phòng thành công. Phòng {old_room_num} đã trở thành trống, phòng {new_room_num} đã được đặt trong {num_days} ngày.")
        else:
            label_ketqua.config(text = label_ketqua.cget("text") + "Số phòng không hợp lệ.")

    enter = Button(Doi_phong,text='Đổi phòng',font='Time 15',pady=12,command=doi_phong)
    enter.grid(row=4, column=1)
    dong5 = Label(Doi_phong,text='Kết quả: ',font='Times 15',height=5)
    dong5.grid(row=5,column=0)

# Hàm hủy phòng
def cancle():
    Huy_phong=tk.Toplevel()
    Huy_phong.title("Hủy phòng")
    Huy_phong.geometry('1000x600+450+120')
    dong1 = Label(Huy_phong,text='Hủy phòng', font='Times 17',height=4)
    dong1.grid(row=0,columnspan=3)
    dong2 = Label(Huy_phong,text='Nhập số phòng cần hủy: ', font='Times 15')
    dong2.grid(row=1,column=0)
    ent_room = Entry(Huy_phong,font='Times 15')
    ent_room.grid(row=1,column=1)
    ent_room.focus()
    def huy_dat_phong():
        room_num = ent_room.get()
        label_ketqua = Label(Huy_phong,text='',font='Times 15')
        label_ketqua.grid(row=7,columnspan=1)     
        if room_num in rooms and "status" in rooms[room_num]:
            label_ketqua.config(text = label_ketqua.cget("text") + "Hủy đặt phòng thành công!")
            del rooms[room_num]["status"]
        else:
            label_ketqua.config(text = label_ketqua.cget("text") + "Phòng chưa được đặt hoặc không tồn tại.")
    enter = Button(Huy_phong,text='Hủy phòng',font='Time 15',pady=12,command=huy_dat_phong)
    enter.grid(row=2, column=1)
    dong3 = Label(Huy_phong,text='Kết quả: ',font='Times 15',height=5)
    dong3.grid(row=3,column=0)

# Hàm thống kê doanh thu
def total_revenue_():
    Doanh_thu=tk.Toplevel()
    Doanh_thu.title("Doanh thu")
    Doanh_thu.geometry('1000x600+450+120')
    dong1 = Label(Doanh_thu,text='Doanh thu', font='Times 17',height=4)
    dong1.grid(row=0,columnspan=3)
    global total_revenue
    total_rooms_booked = 0
    for room_num, room_info in rooms.items():
        if "status" in room_info and room_info["status"] == "đã đặt":
            total_rooms_booked += 1    
    label_ketqua = Label(Doanh_thu,text='',font='Times 15')
    label_ketqua.grid(row=7,columnspan=1)
    label_ketqua.config(text = label_ketqua.cget("text") + f"Tổng số phòng đã đặt: {total_rooms_booked}")
    label_ketqua.config(text = label_ketqua.cget("text") + f"Tổng doanh thu: {total_revenue} đồng.")

#Hàm thoát
def quit():
    win.destroy()

#Chương trình chính
win = Tk()
win.title("LTSN Hotel")
win.geometry('1200x600+230+100')
label1 = Label(win,text = "Chào mừng quý khác đến với \nkhách sạn TLSN",font='Times 30', height=4)
label1.pack()
button1 = Button(win,text="1. Danh sách phòng",font='Times 20', width= 30)
button1.configure(command=list_room)
button1.pack()
button2 = Button(win,text="2. Tìm phòng",font='Times 20', width= 30)
button2.configure(command=find_room)
button2.pack()
button3 = Button(win,text="3. Đặt phòng",font='Times 20', width= 30)
button3.configure(command=check_in)
button3.pack()
button4 = Button(win,text="4. Đổi phòng",font='Times 20', width= 30)
button4.configure(command=change_room)
button4.pack()
button5 = Button(win,text="5. Hủy đặt phòng",font='Times 20', width= 30)
button5.configure(command=cancle)
button5.pack()
button6 = Button(win,text="6. Thống kê doanh thu",font='Times 20', width= 30)
button6.configure(command=total_revenue_)
button6.pack()
button7 = Button(win,text="7. Thoát",font='Times 20', width= 30)
button7.configure(command=quit)
button7.pack()

win.mainloop()
