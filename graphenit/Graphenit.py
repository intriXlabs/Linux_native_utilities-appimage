import customtkinter as ctk
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode('light')
sc="#00A05D"
hc="#00804A"


def set_graph_theme(mode: str):
    if mode == "dark":
        mpl.rcParams.update({
            "text.color": sc,
            "axes.labelcolor": sc,
            "xtick.color": sc,
            "ytick.color": sc,
            "axes.edgecolor": sc,
            "axes.facecolor": "#1f1f1f",
            "figure.facecolor": "#1f1f1f"
        })

    elif mode == "light":
        mpl.rcParams.update({
            "text.color": "black",
            "axes.labelcolor": "black",
            "xtick.color": "black",
            "ytick.color": "black",
            "axes.edgecolor": "black",
            "axes.facecolor": "white",
            "figure.facecolor": "white"
        })


class night_light:
    light=True
    def operation():
        if night_light.light==True:
            night_light.light=False
            ctk.set_appearance_mode('dark')
            night_light_button.configure(text='(')
            ax.set_facecolor('#1f1f1f')
            fig.patch.set_facecolor('#1f1f1f')
            ax.tick_params(colors=sc)
            ax.xaxis.label.set_color(sc)
            ax.yaxis.label.set_color(sc)
            set_graph_theme('dark')
            canvas.draw()
        else:
            night_light.light=True
            ctk.set_appearance_mode('light')
            night_light_button.configure(text='O')
            ax.set_facecolor('white')
            fig.patch.set_facecolor('white')
            ax.tick_params(colors='black')
            ax.xaxis.label.set_color('black')
            ax.yaxis.label.set_color('black')
            set_graph_theme('light')
            canvas.draw()

class graph:
    names=[]
    values=[]
    name_mistake=False
    value_mistake=False
    missmatch=False
    #means it has not previwed if false - true if previwed - also false once a single graph of value had saved - needed reset
    save=False
    def add_name():
        name = names_entry.get().strip()
        if name.isalpha():
            if graph.name_mistake:
                graph.name_mistake = False
                names_add_button.configure(fg_color=sc, hover_color=hc)
            if name in graph.names:
                graph.name_mistake = True
                names_add_button.configure(fg_color='red', hover_color="#AF0000")
                return
            graph.names.append(name)
            names_box.configure(state='normal')
            names_box.insert('end', f'{name}\n')
            names_box.configure(state='disabled')
            names_entry.delete(0, 'end')
        else:
            if not graph.name_mistake:
                graph.name_mistake = True
                names_add_button.configure(fg_color='red', hover_color="#AF0000")
            return

    def add_value():
        value = values_entry.get().strip()
        if value.isdigit():
            if graph.value_mistake:
                graph.value_mistake = False
                values_add_button.configure(fg_color=sc, hover_color=hc)
            graph.values.append(int(value))
            values_box.configure(state='normal')
            values_box.insert('end', f'{value}\n')
            values_box.configure(state='disabled')
            values_entry.delete(0, 'end')
        else:
            if not graph.value_mistake:
                graph.value_mistake = True
                values_add_button.configure(fg_color='red', hover_color="#AF0000")
                return
        
    def preview():
        if len(graph.names)==len(graph.values) and len(graph.names)>=3:
            if graph.missmatch==True:
                graph.missmatch=False
                preview_button.configure(fg_color=sc, hover_color=hc)
            ax.clear()
            ax.bar(graph.names, graph.values, color=sc)
            canvas.draw()
            graph.save=True
        else:
            if graph.missmatch==False:
                graph.missmatch=True
                preview_button.configure(fg_color='red', hover_color="#AF0000")
                return
            
    def save_graph():
        if graph.save==True:
            graph.save=False
            save_button.configure(fg_color=sc, hover_color=hc)
            file_path=filedialog.asksaveasfilename(
                title=('select the folder'),
                filetypes=[('.png', '*.png')]
            )
            graph.save_bar_graph(file_path)
        else:
            save_button.configure(fg_color='red', hover_color="#AF0000")

    def save_bar_graph(file_path):
        DPI = 300
        WIDTH = 3840 / DPI
        HEIGHT = 2160 / DPI

        plt.figure(figsize=(WIDTH, HEIGHT), dpi=DPI)

        plt.bar(graph.names, graph.values, color=sc)
        plt.xlabel("Name")
        plt.ylabel("Value")
        plt.title("Bar Graph")

        plt.tight_layout()
        plt.savefig(
            file_path,
            dpi=DPI,
            bbox_inches="tight"
        )
        plt.close()

    def reset():
        graph.names=[]
        graph.values=[]
        graph.name_mistake=False
        graph.value_mistake=False
        graph.missmatch=False
        graph.save=False
        ax.clear()
        ax.bar(graph.names, graph.values, color=sc)
        canvas.draw()
        names_box.configure(state='normal')
        values_box.configure(state='normal')
        names_box.delete(1.0, 'end')
        values_box.delete(1.0, 'end')
        names_box.configure(state='disabled')
        values_box.configure(state='disabled')



# ------------------- UI here --------------------#
app=ctk.CTk()
app.title('Graphenit')

# ------------------- main two frame - left, right ------------ #
left_window=ctk.CTkFrame(app)
left_window.pack(side='left', fill='both', expand=True)

# imp ### main preiew window
fig = Figure(figsize=(9, 6), dpi=100)
ax = fig.add_subplot(111)

ax.bar(graph.names,graph.values)
ax.set_xlabel("Name")
ax.set_ylabel("Value")

canvas = FigureCanvasTkAgg(fig, master=left_window)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

# button frame
operation_button_frame=ctk.CTkFrame(
    left_window
)
operation_button_frame.pack(side='bottom', fill='both')

#buttons
preview_button=ctk.CTkButton(
    operation_button_frame,
    text='Preview',
    fg_color=sc,
    hover_color=hc,
    command=lambda: graph.preview()
)
preview_button.pack(side='left', padx=20, pady=10)
save_button=ctk.CTkButton(
    operation_button_frame,
    text='Save',
    fg_color=sc,
    hover_color=hc,
    command=lambda: graph.save_graph()
)
save_button.pack(side='right', padx=20, pady=10)

# -------------------- right one ------------------------ #
right_window=ctk.CTkFrame(app)
right_window.pack(side='right', fill='both')
# name frame
name_window=ctk.CTkFrame(right_window)
name_window.pack(fill='x')
# name text
name_label=ctk.CTkLabel(
    name_window, 
    text='Graphenit by IntrixLabs',
    corner_radius=10
)
name_label.pack(pady=10, padx=10, side='left')
night_light_button=ctk.CTkButton(
    name_window, 
    text='O',
    width=1,
    fg_color='transparent',
    text_color='grey',
    hover_color=hc,
    command=lambda: night_light.operation()
)
night_light_button.pack(side='right', padx=10, pady=10)

# ---------------------------------- graph name frame
graph_name_frame=ctk.CTkFrame(
    right_window,
    corner_radius=10
)
graph_name_frame.pack(pady=10, padx=10)
temp_label=ctk.CTkLabel(
    graph_name_frame,
    text='Name Section'
).pack(pady=5, padx=5)
names_box=ctk.CTkTextbox(
    graph_name_frame,
    state='disabled'
)
names_box.pack(pady=5, padx=5)
names_entry=ctk.CTkEntry(
    graph_name_frame,
    border_color=sc,
    text_color=sc
)
names_entry.pack(pady=5, padx=5)
names_add_button=ctk.CTkButton(
    graph_name_frame,
    text='Add',
    fg_color=sc,
    hover_color=hc,
    command=lambda:graph.add_name()
)
names_add_button.pack(pady=10, padx=10)

# ------------------------------------ graph value frame
graph_value_frame=ctk.CTkFrame(
    right_window,
    corner_radius=10
)
graph_value_frame.pack(pady=10, padx=10)
temp_label=ctk.CTkLabel(
    graph_value_frame,
    text='value Section'
).pack(pady=5, padx=5)
values_box=ctk.CTkTextbox(
    graph_value_frame,
    state='disabled'
)
values_box.pack(pady=5, padx=5)
values_entry=ctk.CTkEntry(
    graph_value_frame,
    border_color=sc,
    text_color=sc
)
values_entry.pack(pady=5, padx=5)
values_add_button=ctk.CTkButton(
    graph_value_frame,
    text='Add',
    fg_color=sc,
    hover_color=hc,
    command=lambda: graph.add_value()
)
values_add_button.pack(pady=10, padx=10)

reset_button=ctk.CTkButton(
    right_window,
    text='reset',
    fg_color=sc,
    hover_color=hc,
    command=lambda: graph.reset()
)
reset_button.pack(padx=20, pady=10)

app.mainloop()