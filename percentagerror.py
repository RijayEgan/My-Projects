def PercentageERROR():
  experimental_value = float(input("Enter the Experimental Value Here: "));
  theoretical_value = float(input("Enter the Theoretical Value Here: "));
  subractedvalue = float(theoretical_value - experimental_value);
  divident = float(abs(subractedvalue)/theoretical_value);
  percentage_error = float(divident * 100)       
  print(round(percentage_error), "percent is the Percentage error")



PercentageERROR()