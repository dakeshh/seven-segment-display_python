
LED="""
### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 
"""
inp = input("Please enter nnumber to be displied = ")

r1_inp = ["0", "2", "3", "5", "6", "7", "8", "9"]  # print ###
r2_inp = ["0", "4", "8", "9"]
r4_inp = ["0", "6", "8"]


def r1_inp_fn(inp_fn):
     st = False;
     for r1_inp_f in r1_inp:
          if inp_fn in r1_inp_f:
               st = True;
               break;
     return st;

def r2_inp_fn(inp_fn):
     st = False;
     for r2_inp_f in r2_inp:
          if inp_fn in r2_inp_f:
               st = True;
               break;
     return st;

def r4_inp_fn(inp_fn):
     st = False;
     for r4_inp_f in r4_inp:
          if inp_fn in r4_inp_f:
               st = True;
               break;
     return st;

for r1 in range(5):
     for c1 in range(len(inp)):

          if (r1 == 0 or r1 == 2 or r1 == 4) and r1_inp_fn(inp[c1]):
                    if r1 == 2 and inp[c1] == "0":
                         print("{}".format("# #"), end="")
                    elif inp[c1] == "7" and (r1 == 2 or r1 == 4):
                         print("{}".format("  #"), end="");
                    else:
                         print("{}".format("###"), end="");
          elif (r1 == 0 or r1 == 2 or r1 == 4) and inp[c1] == "1":
               print("{}".format("  #"), end="")
          elif (r1 == 0 ) and inp[c1] == "4":
               print("{}".format("# #"), end="");
          elif r1 == 2 and inp[c1] == "4":
               print("{}".format("###"), end="");
          elif r1 == 4 and inp[c1] == "4":
               print("{}".format("  #"), end="");

          if (r1 == 1) and r2_inp_fn(inp[c1]):
               print("{}".format("# #"), end="");
          elif (r1 == 1) and (inp[c1] == "1" or inp[c1] == "2" or inp[c1] == "3" or inp[c1] == "7"):
               print("{}".format("  #"), end="");
          elif (r1 == 1) and (inp[c1] == "5" or inp[c1] == "6"):
               print("{}".format("#  "), end="")

          if (r1 == 3) and r4_inp_fn(inp[c1]):
               print("{}".format("# #"), end="");
          elif (r1 == 3) and (inp[c1] == "1" or inp[c1] == "3" or inp[c1] == "4" or inp[c1] == "5" or inp[c1] == "7" or inp[c1] == "9"):
               print("{}".format("  #"), end="");
          elif (r1 == 3) and (inp[c1] == "2"):
               print("{}".format("#  "), end="")

          print(end="  ");
     print("");

if r1 == 1 and r1_inp_fn(inp[0]):
     print("{}".format("#"), end="")
else:
     print("{}".format(" "), end="")

