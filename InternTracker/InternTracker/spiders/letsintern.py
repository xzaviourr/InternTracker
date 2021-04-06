import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import LetsInternItem
from InternTracker.spiders.logger import letsintern_logger
import json
import requests
import csv 
class LetsIntern(scrapy.Spider):
    #name and domain of the scraper
    name = "letsintern"
    allowed_domains = ["https://www.letsintern.com/"]
    start_urls = [str("https://www.letsintern.com/filterInternshipsAJAX?filterData%5BjobType%5D=&filterData%5Blocation%5D=&filterData%5BjobCategory%5D=7%2C56%2C57%2C58%2C61%2C64%2C65%2C66%2C67%2C68%2C69%2C102%2C157%2C164%2C165%2C166%2C168%2C169%2C171%2C175%2C179%2C182%2C184%2C185%2C197%2C784%2C923%2C932%2C934%2C972%2C983%2C984%2C985%2C987%2C988%2C989%2C990%2C992%2C993%2C994%2C997%2C1035%2C1036%2C1042%2C1043%2C1071%2C1078%2C1079%2C1083%2C1084%2C1085%2C1086%2C1087%2C1088%2C1089%2C1090%2C1091%2C1092%2C1093%2C1094%2C1095%2C1096%2C1106%2C1107%2C1108%2C1109%2C1114%2C1115%2C1116%2C1117%2C1118%2C1119%2C1120%2C1121%2C1122%2C1123%2C1124%2C1125%2C1126%2C1127%2C1128%2C1129%2C1130%2C1138%2C1139%2C1140%2C1141%2C1142%2C1143%2C1144%2C1145%2C1146%2C1147%2C1148%2C1149%2C1150%2C1151%2C1152%2C1153%2C1154%2C1156%2C1157%2C1158%2C1159%2C1161%2C1162%2C1163%2C1164%2C1165%2C1166%2C1167%2C1168%2C1169%2C1170%2C1171%2C1172%2C1173%2C1174%2C1175%2C1176%2C1177%2C1178%2C1179%2C1180%2C1183%2C1184%2C1186%2C1192%2C1193%2C1194%2C1195%2C1196%2C1197%2C1198%2C1199%2C1200%2C1201%2C1202%2C1203%2C1204%2C1205%2C1206%2C1207%2C1208%2C1209%2C1210%2C1211%2C1212%2C1213%2C1214%2C1215%2C1216%2C1217%2C1218%2C1219%2C1220%2C1221%2C1222%2C1223%2C1224%2C1225%2C1226%2C1227%2C1228%2C1229%2C1230%2C1231%2C1232%2C1233%2C1238%2C1239%2C1240%2C1241%2C1242%2C1243%2C1244%2C1245%2C1246%2C1247%2C1248%2C1249%2C1250%2C1251%2C1252%2C1253%2C1254%2C1255%2C1256%2C1257%2C1258%2C1259%2C1261%2C1262%2C1263%2C1264%2C1265%2C1266%2C1267%2C1269%2C1270%2C1271%2C1272%2C1273%2C1285%2C1286%2C1287%2C1288%2C1289&filterData%5Bavailability%5D=&filterData%5Bsearch%5D=&filterData%5Bskill%5D=&filterData%5Bposted%5D=&offset_all=1&limit_all=10000")]

    custom_settings={'ITEM_PIPELINES' : {
        'InternTracker.pipelines.InterntrackerPipeline': 300,
        'InternTracker.pipelines.CsvPipeline': 500}}
    
    def parse(self, response):      
        #Url to fetch the data
        url="https://www.letsintern.com/filterInternshipsAJAX?filterData%5BjobType%5D=&filterData%5Blocation%5D=&filterData%5BjobCategory%5D=7%2C56%2C57%2C58%2C61%2C64%2C65%2C66%2C67%2C68%2C69%2C102%2C157%2C164%2C165%2C166%2C168%2C169%2C171%2C175%2C179%2C182%2C184%2C185%2C197%2C784%2C923%2C932%2C934%2C972%2C983%2C984%2C985%2C987%2C988%2C989%2C990%2C992%2C993%2C994%2C997%2C1035%2C1036%2C1042%2C1043%2C1071%2C1078%2C1079%2C1083%2C1084%2C1085%2C1086%2C1087%2C1088%2C1089%2C1090%2C1091%2C1092%2C1093%2C1094%2C1095%2C1096%2C1106%2C1107%2C1108%2C1109%2C1114%2C1115%2C1116%2C1117%2C1118%2C1119%2C1120%2C1121%2C1122%2C1123%2C1124%2C1125%2C1126%2C1127%2C1128%2C1129%2C1130%2C1138%2C1139%2C1140%2C1141%2C1142%2C1143%2C1144%2C1145%2C1146%2C1147%2C1148%2C1149%2C1150%2C1151%2C1152%2C1153%2C1154%2C1156%2C1157%2C1158%2C1159%2C1161%2C1162%2C1163%2C1164%2C1165%2C1166%2C1167%2C1168%2C1169%2C1170%2C1171%2C1172%2C1173%2C1174%2C1175%2C1176%2C1177%2C1178%2C1179%2C1180%2C1183%2C1184%2C1186%2C1192%2C1193%2C1194%2C1195%2C1196%2C1197%2C1198%2C1199%2C1200%2C1201%2C1202%2C1203%2C1204%2C1205%2C1206%2C1207%2C1208%2C1209%2C1210%2C1211%2C1212%2C1213%2C1214%2C1215%2C1216%2C1217%2C1218%2C1219%2C1220%2C1221%2C1222%2C1223%2C1224%2C1225%2C1226%2C1227%2C1228%2C1229%2C1230%2C1231%2C1232%2C1233%2C1238%2C1239%2C1240%2C1241%2C1242%2C1243%2C1244%2C1245%2C1246%2C1247%2C1248%2C1249%2C1250%2C1251%2C1252%2C1253%2C1254%2C1255%2C1256%2C1257%2C1258%2C1259%2C1261%2C1262%2C1263%2C1264%2C1265%2C1266%2C1267%2C1269%2C1270%2C1271%2C1272%2C1273%2C1285%2C1286%2C1287%2C1288%2C1289&filterData%5Bavailability%5D=&filterData%5Bsearch%5D=&filterData%5Bskill%5D=&filterData%5Bposted%5D=&offset_all=31&limit_all=10000"

        #request made here
        try:
            r=(requests.get(url)).json()
        except:
            letsintern_logger.error("Error in making request")

        '''There are 2 lists for the 2 types of jobs: featured and non-featured'''
        #extracting data from list of featured jobs
        featured=len(r["resp"]["data"]["featured_jobs"])
        for i in range(featured):
            posting = LetsInternItem()
            posting['job_no']=i+1
            posting['role'] =r["resp"]["data"]["featured_jobs"][i]["_source"]["Title"]
            posting['company'] = r["resp"]["data"]["featured_jobs"][i]["_source"]["CompanyName"]
            posting['location'] = r["resp"]["data"]["featured_jobs"][i]["_source"]["locationStr"]
            posting['start_date'] = (r["resp"]["data"]["featured_jobs"][i]["_source"]["StartDate"][0:10])
            posting['end_date'] = (r["resp"]["data"]["featured_jobs"][i]["_source"]["EndDate"][0:10])
            posting['deadline'] = (r["resp"]["data"]["featured_jobs"][i]["_source"]["ApplicationDeadline"][0:10])
            pay = str(r["resp"]["data"]["featured_jobs"][i]["_source"]["Amount"])
            if '-' in pay:
                pay=pay.split("-")         #breaking stipend into max and min
            else:
                pay=list(pay)
            posting['stipendmin'] = pay[0]
            posting['stipendmax'] = pay[-1]
            posting["link"]="https://www.letsintern.com"+r["resp"]["data"]["featured_jobs"][i]["_source"]["publicLink"]
            yield posting
        
        #extracting data from list of non-featured jobs
        non_featured=len(r["resp"]["data"]["jobs"])
        for i in range(non_featured):
            posting = LetsInternItem()
            posting['job_no']=featured+i+1
            posting['role'] =r["resp"]["data"]["jobs"][i]["_source"]["Title"]
            posting['company'] = r["resp"]["data"]["jobs"][i]["_source"]["CompanyName"]
            posting['location'] = r["resp"]["data"]["jobs"][i]["_source"]["locationString"]
            posting['start_date'] = (r["resp"]["data"]["jobs"][i]["_source"]["StartDate"][0:10])
            posting['end_date'] = (r["resp"]["data"]["jobs"][i]["_source"]["EndDate"][0:10])
            posting['deadline'] = (r["resp"]["data"]["jobs"][i]["_source"]["ApplicationDeadline"][0:10])
            pay = str(r["resp"]["data"]["jobs"][i]["_source"]["Amount"])
            if '-' in pay:                            #breaking stipend into max and min
                pay=pay.split("-")
            else:
                pay=list(pay)
            posting['stipendmin'] = pay[0]
            posting['stipendmax'] = pay[-1]
            posting["link"]="https://www.letsintern.com"+r["resp"]["data"]["jobs"][i]["_source"]["publicLink"]
            yield posting
        

        