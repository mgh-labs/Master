
#   Welcome to the Tube Filling Volume Calculator
#   For tubes filled on the hand fill and mixmaster filling lines

#   UOM:
#   lbl_vol = mL
#   rgt_min = g
#   rgt_tgt = g
#   rgt_max = g
#   bom_vol = mL

#   Collect label volume from user

#   -
#   Insert automated find label volume function here
#   -

lbl_vol = float(input('Please enter the label volume in mL: '))

#   -
#   Insert automated find BOM volume function here
#   -

#   -
#   Insert automated find density function here
#   -

density = float(input('Please enter density in g/mL: '))

#   Calculate rgt_min,  

rgt_min = lbl_vol*density

#   Calculate rgt_tgt, rgt_max condinionally

if lbl_vol <= 0.2:                      #   lbl_vol < 0.2mL (200uL)
    rgt_tgt = rgt_min*1.2
    rgt_max = rgt_min*1.4
elif lbl_vol > 0.2 and lbl_vol <= 2:    #   0.2mL  < lbl_vol <= 2mL
    rgt_tgt = rgt_min*1.1
    rgt_max = rgt_min*1.2
elif lbl_vol > 2:                       #   lbl_vol > 2mL 
    rgt_tgt = rgt_min*1.05
    rgt_max = rgt_min*1.1

#   Calculate BOM volume

bom_vol = rgt_tgt/density

#   Apply precision to record and rounding rules to calculated volumetric values 

#   Round rgt tgt

if rgt_tgt <= 0.01:
    rgt_tgt = round(rgt_tgt, 5)
elif rgt_tgt > 0.01 and rgt_tgt <= 0.2:
    rgt_tgt = round(rgt_tgt, 4)
elif rgt_tgt > 0.2 and rgt_tgt <= 2:
    rgt_tgt = round(rgt_tgt, 3)
elif rgt_tgt > 2 and rgt_tgt <= 5:
    rgt_tgt = round(rgt_tgt, 2)


#   Round rgt max

if rgt_max <= 0.01:
    rgt_max = round(rgt_max, 5)
elif rgt_max > 0.01 and rgt_max <= 0.2:
    rgt_max = round(rgt_max, 4)



#   Send data to table and print results

from beautifultable import BeautifulTable
table = BeautifulTable()
table.rows.append([lbl_vol,density,rgt_min,rgt_tgt,rgt_max,bom_vol])

table.columns.header = ["Label Volume (mL)","Reagent Density (g/mL)","Reagent Minimum Spec (mL)","Reagent Target Spec (mL)","Reagent Maximum Spec (mL)","BOM Volume (mL)"]
print(table)

#   Format float output to use 


