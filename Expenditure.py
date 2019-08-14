from tkinter import *


cost_category = {
    "Management Fees": 23000,
    "Service Charge Audit Fees": 23005,
    "Site Management Resources (Gen)": 23015,
    "Staff Costs": 23016,
    "Receptionists": 23017,
    "Site Accommodation Rent": 23018,
    "Site Accommodation Telephone": 23020,
    "Site Accommodation Stationary": 23021,
    "H&S Audits": 23030,
    "Gas": 23050,
    "Water": 23065,
    "Security Contracts": 23070,
    "Security Systems": 23071,
    "Internal Cleaning": 23081,
    "Window Cleaning": 23083,
    "Hygiene Services/toiletries": 23084,
    "Waste Management": 23085,
    "Seasonal decorations": 23087,
    "Internal displays": 23088,
    "Events": 23100,
    "M&E Contract": 23110,
    "M&E Repairs": 23111,
    "Life Safety Systems": 23113,
    "Lift Maintenance": 23125,
    "Lift Repairs": 23126,
    "Lift Consultancy": 23127,
    "Suspended Access Equipment Maintenance": 23140,
    "Suspended Access Repairs": 23141,
    "Internal Repairs & Maintenance": 23150,
    "External Repairs": 23150,
}

code_ratio = {
    23000: {'sch1': 100},
    23005: {'sch1': 100},
    23015: {'sch1': 53.9,
            'sch2': 46.1},
    23016: {'sch1': 39,
            'sch2': 59,
            'sch3': 2},
    23017: {'sch2': 100},
    23018: {'sch1': 100},
    23020: {'sch1': 88,
            'sch3': 12},
    23021: {'sch1': 100},
    23030: {'sch1': 85,
            'sch2': 15},
    23050: {'sch2': 100},
    23065: {'sch2': 100},
    23070: {'sch1': 93,
            'sch3': 3.5,
            'sch4': 3.5},
    23071: {'sch1': 23,
            'sch2': 55,
            'sch4': 8,
            'sch6': 14},
    23081: {'sch1': 1.04,
            'sch2': 98.96},
    23083: {'sch1': 100},
    23084: {'sch2': 100},
    23085: {'sch1': 61,
            'sch2': 19,
            'sch6': 10},
    23087: {'sch2': 100},
    23088: {'sch2': 100},
    23100: {'sch2': 100},
    23110: {'sch1': 5,
            'sch2': 90,
            'sch4': 5},
    23111: {'sch1': 5,
            'sch2': 90,
            'sch4': 5},
    23113: {'sch2': 94,
            'sch4': 6},
    23125: {'sch5': 100},
    23126: {'sch5': 100},
    23127: {'sch5': 100},
    23140: {'sch2': 100},
    23141: {'sch2': 100},
    23150: {'sch2': 100},
    23151: {'sch1': 48,
            'sch2': 52}
}

global exp_calc
global e1
global e2

def get_expense():

    # Get value from Entrybox
    e1 = readin.get()
    # Get value from optionbox
    e2 = variable.get()
    # Check optionbox value and output to label the value
    for cat in cost_category.keys():
        if cat == e2:
            cat_lab.set(cost_category[cat])
            exp_calc = cost_category[cat]
    calc_sch(exp_calc, e1)


def calc_sch(exp_calc, e1):
    sch1.set(" ")
    sch2.set(" ")
    sch3.set(" ")
    sch4.set(" ")
    sch5.set(" ")
    sch6.set(" ")

    if exp_calc in code_ratio.keys():

        if 'sch1' in code_ratio[exp_calc]:
            val = e1 * (code_ratio[exp_calc]['sch1'] / 100)
            sch1.set(f"£{round(val, 2)}")
            Label(root, text="Schedule 1:", borderwidth=2, relief="groove").grid(row=1, column=3, sticky=W+E)
            Label(root, textvariable=sch1, borderwidth=2, relief="groove").grid(row=1, column=4, sticky=W+E)

        if 'sch2' in code_ratio[exp_calc]:
            val = e1 * (code_ratio[exp_calc]['sch2'] / 100)
            sch2.set(f"£{round(val, 2)}")
            Label(root, text="Schedule 2:", borderwidth=2, relief="groove").grid(row=2, column=3, sticky=W+E)
            Label(root, textvariable=sch2, borderwidth=2, relief="groove").grid(row=2, column=4, sticky=W+E)

        if 'sch3' in code_ratio[exp_calc]:
            val = e1 * (code_ratio[exp_calc]['sch3'] / 100)
            sch3.set(f"£{round(val, 2)}")
            Label(root, text="Schedule 3:", borderwidth=2, relief="groove").grid(row=3, column=3, sticky=W+E)
            Label(root, textvariable=sch3, borderwidth=2, relief="groove").grid(row=3, column=4, sticky=W+E)

        if 'sch4' in code_ratio[exp_calc]:
            val = e1 * (code_ratio[exp_calc]['sch4'] / 100)
            sch4.set(f"£{round(val, 2)}")
            Label(root, text="Schedule 4:", borderwidth=2, relief="groove").grid(row=4, column=3, sticky=W+E)
            Label(root, textvariable=sch4, borderwidth=2, relief="groove").grid(row=4, column=4, sticky=W+E)

        if 'sch5' in code_ratio[exp_calc]:
            val = e1 * (code_ratio[exp_calc]['sch5'] / 100)
            sch5.set(f"£{round(val, 2)}")
            Label(root, text="Schedule 5:", borderwidth=2, relief="groove").grid(row=5, column=3, sticky=W+E)
            Label(root, textvariable=sch5, borderwidth=2, relief="groove").grid(row=5, column=4, sticky=W+E)

        if 'sch6' in code_ratio[exp_calc]:
            val = e1 * (code_ratio[exp_calc]['sch6'] / 100)
            sch6.set(f"£{round(val, 2)}")
            Label(root, text="Schedule 6:", borderwidth=2, relief="groove").grid(row=6, column=3, sticky=W+E)
            Label(root, textvariable=sch6, borderwidth=2, relief="groove").grid(row=6, column=4, sticky=W+E)


root = Tk()
root.geometry("+200+200")
root.title('Cost Category Breakdown')
root.configure(background='white', padx=40, pady=40)

# Entry box variable
readin = IntVar()
# Drop down variable
variable = StringVar()
# Declare variable for the Cat label
cat_lab = StringVar()
# Declare schedule variables
sch1 = StringVar()
sch2 = StringVar()
sch3 = StringVar()
sch4 = StringVar()
sch5 = StringVar()
sch6 = StringVar()

Label(root, text="Enter expense amount (£):",fg='white', borderwidth=2, relief="groove", bg='grey', width=25, bd=2,
          font=("Helvetica", 12)).grid(row=0, column=0, sticky=W+E)
Label(root, text="Cost Category",fg='white', borderwidth=2, relief="groove", bg='grey', width=25, bd=2,
          font=("Helvetica", 12)).grid(row=0, column=1, sticky=W+E)
Label(root, text="Cost Code",fg='white', borderwidth=2, relief="groove", bg='grey', width=25, bd=2,
          font=("Helvetica", 12)).grid(row=0, column=2, sticky=W+E)
Label(root, text="Schedules",fg='white', borderwidth=2, relief="groove", bg='grey', width=25, bd=2,
          font=("Helvetica", 12)).grid(row=0, column=3, columnspan=2, sticky=W+E)

Entry(root, textvariable=readin).grid(row=1, column=0, sticky=W+E)
b1 = Button(root, text='Submit', command=get_expense).grid(row=2, column=0, sticky=W+E)

# Drop down box to select expense description
variable.set("Select Cost Category") # default value
OptionMenu(root, variable, *cost_category).grid(row=1, column=1)

# Output label dependent on drop down selection
Label(root, textvariable=cat_lab).grid(row=1, column=2)




root.mainloop()