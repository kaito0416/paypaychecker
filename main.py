import paybase,time
print("PayPayLinkChecker\nDeveloped by Kodai.")
txt_name=https://waki285.github.io/paypaygen/try:
  f=open(txt_name,"r")
  paylink=f.read().split('\n')
  paylink=([i for i in paylink if i != ""])
  print(paylink)
  f.close()
except:
  print("読み込めませんでした。")
  exit()
hozon=input("workedなリンクの保存先を入力してください。\n拡張子は入力しなくてよいです。\n>>")
delay1=input("Delayを入力してください。\nおすすめは3です(秒)。0にするとIPが死ぬかも？\n>>")
try:
  delay1=int(delay1)
except:
  print("Delayでは数字を指定してください。")
  exit()
for i in paylink:
  paybase.check(i,hozon)
  time.sleep(delay1)
print("終了")
