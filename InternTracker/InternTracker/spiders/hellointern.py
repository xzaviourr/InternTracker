import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting

def dateformat(date) :
    date=date.split(" ")
    months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sept':'09','Oct':'10','Nov':'11','Dec':'12'}
    if len(date[0]) == 1 :
        date[0] = '0' + date[0]
    correct = date[0] + '-' + months[date[1]] + '-' + date[2]
    return correct

def dateformat2(s) :
    print(s)
    s=s.split(" ")
    months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sept':'09','Oct':'10','Nov':'11','Dec':'12'}
    if len(s[1]) == 1 :
        s[1] = '0' + s[1]
    correct = s[1] + '-' + months[s[0]] + '-' + s[2]
    return correct

class Hellointern(scrapy.Spider) :

    name = "hellointern_spy"
    start_urls =["https://www.hellointern.com/search/by_filters"]
    close_spider = False
    
    def parse(self, response) :

        # Closes the spider if record already scraped before
        if self.close_spider :
            raise CloseSpider(reason = "ALREADY SCRAPED")
        roles = response.css('.title_salary span a::text').getall()
        companies = response.css(".name_span a::text").getall()
        locations = response.css(".location_span::text").getall()   
        locations = [x.replace('End Date: ','').replace("\r\n","").strip() for x in locations]
        locations=locations[0::2]
        start_dates = response.css(".salary_span b::text").getall()
        start_dates=[x.replace(",","").strip() for x in start_dates]
        stipends = response.css(".salary_span::text").getall()  
        stipends=[x.replace('Start Date: ','').replace("Unpaid","0").replace("","0").replace("(per month)","").strip() for x in stipends]
        stipends=stipends[0::2]
        link=response.css(".title_span a::attr(href)").getall()
        posting_date=response.css(".day::text").getall()
        posting_my=response.css(".month_year::text").getall()    
        date=[]
        #end_date=resposne.css(".location_span b").getall()
        for i in range(len(roles)):
            date.append(posting_date[i]+ " " + posting_my[i])
            date[i]=dateformat(date[i])
        
        for i in range(len(roles)):
            start_dates[i]=dateformat2(start_dates[i])
        
        for i in range(len(roles)):
            posting = InternshipPosting()
            posting['role'] = roles[i]
            posting['company_name'] = companies[i]
            posting['location'] = locations[i]
            posting['start_date'] = start_dates[i]
            posting['stipendmin']= int(stipends[i].strip().split(" ")[0])
            posting['stipendmax']= int(stipends[i].strip().split(" ")[0])
            posting['deadline'] = ""#dateformat(deadlines[i])
            posting['link'] = "https://www.hellointern.com" + link[i]
            posting['number_of_applicants'] = 0
            posting['posting_date'] = date[i]
            posting['category_id'] = 0
            yield posting
