def main():
 month_list = ['Juanary', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
 #define a dictionary that will have the month name and month sales
 dic={}
 for month_name in month_list:
  dic[month_name] = float(input('Enter the sales for '+month_name))
 print('Total sales:', sum(dic.values()))
 avg = sum(dic.values()) / len(dic)
 print('Average sales: %.2f ' % avg)
 print('Highest sales :', max(dic, key=dic.get))
 print('Lowest sales : ', min(dic, key=dic.get))
main()
