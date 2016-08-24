import urllib.request
import json
lvl_exp = [0,68,364,1169,2885,6039,11288,19424,31379,48230,71203,101678,141194,191455,254331,331868,
           426289,540001,675597,835864,1023785,1439215,1948497,2568850,3320625,4227172,5315161,6614929,
           8161929,9995812,12162655,14713777,17708475,21213445,25304463,30067485,35599858,42010312,
           49421366,57972427,67818553,79135431,92117896,106985763,123986756,143394645,165516618,
           190696911,219317613,251805374,288635909,330338848,377507026,430790086,490916803,558693890,
           635018116,720879370,817380319,925741335,1047311009,1183577349,1336187067,1506967658,
           1697936136,1911306680,2149533465,2415323168,2711646440,3041801165,3409398455,3818421441,
           4273257148,4778730308,5340152664,5963335189,7138805250,9372198366,16072377713,38406308871]

def get_json_from_url(date):
    urlData = "http://tpalp.ru/l2c/" + date + ".l2cl_chars.ratings.characters.json"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))


def get_lvl_for_exp(cur_exp):
    cur_lvl = 0
    for lvl in lvl_exp:
        if cur_exp > lvl :
            cur_lvl = cur_lvl + 1
    return cur_lvl


def get_persent_for_exp(cur_exp):
    cur_lvl = get_lvl_for_exp(cur_exp)
    return (cur_exp-lvl_exp[cur_lvl-1])/(lvl_exp[cur_lvl]-lvl_exp[cur_lvl-1])

def get_diff_in_percent_for_exp(start_exp , end_exp):
    return (get_lvl_for_exp(end_exp)+get_persent_for_exp(end_exp))-(get_lvl_for_exp(start_exp)+get_persent_for_exp(start_exp))

def print_info_for_rmt_table(date,char_nicks):
    exp_data = get_json_from_url(date)
    print("\nData for copy-pasting to RMT exp table. Date: %s" % (date))
    for p_member in char_nicks:
         for x in exp_data:
            if (x["char"] == p_member)&(x["server"]=="Gran Kain"):
                print (x["exp_cnt"])


def print_readable_exp_info(date,char_nicks):
    exp_data = get_json_from_url(date)
    print("\nCurrent exp data for %s" % (date))
    for p_member in char_nicks:
         for x in exp_data:
            if (x["char"] == p_member)&(x["server"]=="Gran Kain"):
                print ("%16s \t %d \t %5.2f" % (x["char"],
                                                get_lvl_for_exp(int(x["exp_cnt"])) ,
                                                get_persent_for_exp(int(x["exp_cnt"]))*100 ))


def print_percent_diff_info(start_date,end_date,char_nicks):
    exp_data = get_json_from_url(start_date)
    exp_end_data = get_json_from_url(end_date)
    print("\nDiff tabble for persents on chars. \nStart date %s end date %s" % (start_date,end_date))
    for p_member in char_nicks:
         for x in exp_data:
            if (x["char"] == p_member)&(x["server"]=="Gran Kain"):
                for y in exp_end_data:
                    if (y["char"] == p_member)&(y["server"]=="Gran Kain"):
                        print ("%16s \t %d \t %5.2f" % (x["char"],get_lvl_for_exp(int(x["exp_cnt"])) ,get_diff_in_percent_for_exp(int(x["exp_cnt"]),int(y["exp_cnt"]))*100   ))

def print_info_for_excel    (char_nicks):
    print(" ",end="\t")
    for dday in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]:
        for dtime in ["_06-30","_18-30"]:
            print("02-%s%s" % (dday,dtime),end="\t")
    print("")
    for p_member in char_nicks:
        print (p_member, end="\t")
        for dday in ["01","02","03","04","05","06","07","08","09","10","11"]:
            for dtime in ["_06-30","_18-30"]:
                date="2016-02-" + dday + dtime
                exp_data = get_json_from_url(date)
                for x in exp_data:
                    if (x["char"] == p_member)&(x["server"]=="Gran Kain"):
                        print (x["exp_cnt"],end="\t")
        print("")


def print_char_info_for_all    (char_nicks):
    for p_member in char_nicks:
        print (p_member, end="\t")
    print("")
    for dmounth in ["02","03","04","05","06","07","08"]:
        for dday in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]:
            for dtime in ["18-30"]:
                date="2016-"+dmounth+"-" + dday +"_"+ dtime
                print(date,end="\t")
                try:
                    exp_data = get_json_from_url(date)
                except:
                    print ("no data")
                else:
                    for p_member in char_nicks:
                        try:
                            for x in exp_data:
                                if (x["char"] == p_member)&(x["server"]=="Gran Kain"):
                                    print ("%5.4f" % ( get_lvl_for_exp(int(x["exp_cnt"])) + get_persent_for_exp(int(x["exp_cnt"]))),end="\t")
                        except:
                            print (" ",end="\t")
                    print("")



rr_party_members = ["iProrok","Cartes","Alter","M1ST1KA","Shat","Rosie","Nertea","Tirael","Lanza","Икона","SWave"]
rr_party = ["iProrok","Cartes","Alter","M1ST1KA","Shat","Nertea","Икона","Lanza","SWave","Santinel","Tirael","Pony","ZanKoy","IndependenT","VASIAPROFET","Mist1ka","Santinel"]
sent_party = ["Amaranthine", "Andori", "Ashrada", "TaRaKaH", "Адиабата", "OgreMage", "ToMCoHl", "Lainara", "Muriel", "Ultrox", "Jfoo"]
avtsh_party = ["Avotinsh","Agma","m1RC","iPe4enka","Бонифаций","KOLLlAPA","KOLLIAPA","YersiniaPestis","Balloon","meh","Neue","Cavalier","iGodBlessMyAss","CubaLibre","gavi","Qisa","Marimo","Addax","MenOfHell","Rmpg","Neue","Merula"]
rr_aq_twinks = ["Security","Lissari","Todeslicht","Smiley","Miromax","Einecawir","FireDevil","To1v1CoH","Ascaf","ЗажиГалька","Kaworu"]
fast_party = ["XyZzz","FemmeFatale", "Ersh","Gekate","Medika","Berz","Викторовна","Aiswill","iGoodgame","Odair","Xy3", "Reinne","lShiza"]
anchor_party = ["ЛосярО","Bugs","Ruiz","CrazyDope","DarkW1zard","AbsoluteEvil","PM"]
piha_party = ["PihaStyle","Juster","DarkPassion","z0omik","Кристен","KarinaWhite","nagibaka","EFka","iEurope","nilaj"]
VALLORA= ["Vallora"]

MyTwinks=["Lanza","BadBoy","sLOns","Shatalter"]
#print_info_for_rmt_table("2016-02-20_06-30", rr_party_members)
#print_info_for_excel(rr_full_pm)
#input('Waiting a key...')

dd_party=rr_party
dd_start="2016-06-30_06-30"
dd_end="2016-07-30_06-30"
#print(dd_party)
#print_readable_exp_info(dd_end, dd_party)
#print_percent_diff_info(dd_start,dd_end,dd_party)

print_char_info_for_all(MyTwinks)