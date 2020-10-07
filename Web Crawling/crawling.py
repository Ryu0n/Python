import csv

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def initialize_selenium():
    # Selenium
    driver = webdriver.Chrome('C:/Users/gksth/Downloads/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(3)
    return driver

def mk_csv(datas, filename):
    datas = list(set(datas)) # remove duplication
    with open(filename, 'w', encoding='euc-kr', newline='') as output:
        writer = csv.writer(output)

        for data in datas:
            writer.writerow(data)

def crawling_workNet(driver):
    # move to workNet
    driver.get('https://www.work.go.kr/seekWantedMain.do')

    # login
    login = driver.find_element_by_link_text('로그인').get_attribute('href')
    driver.get(login)

    ID = 'weatleking'
    PW = 'ryuon6807!'

    chkBox = driver.find_element_by_id('chkKeyboard1')
    chkBox.click()

    ID_input = driver.find_element_by_xpath("//form[@id='indivLoginForm']/div[@class='login-input']/input[@id='custId1']")
    PW_input = driver.find_element_by_xpath("//form[@id='indivLoginForm']/div[@class='login-input']/input[@id='pwd1']")


    ID_input.click(); sleep(0.5)
    ID_input.send_keys(ID)

    PW_input.click(); sleep(0.5)
    PW_input.send_keys(PW)

    login_btn = driver.find_element_by_xpath("//button[@class='button blue']")
    login_btn.click()

    driver.get('https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=133207&rot2WorkYn=&templateInfo=&payGbn=&resultCnt=10&keywordJobCont=&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=job&actServExcYn=&keywordStaAreaNm=&maxPay=&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&resultCntInfo=10&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=&searchOn=Y&subEmpHopeYn=&academicGbn=&foriegn=&templateDepthNoInfo=&mealOfferClcd=&station=&moerButtonYn=&holidayGbn=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=&stationNm=&benefitGbn=&keywordFlag=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=5d8b1778-9610-43c7-b253-f963f887b957&keywordBusiNm=&preferentialGbn=all&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=1&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL')

    last_page = driver.find_element_by_xpath("//div[@class='paging_direct']").text.split('/')[-1].split('바로가기')[0].strip()

    datas = []
    for page in range(1, int(last_page)+1):
        print('page number : ', page)
        print('datas : ', datas)
        lnk = 'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=133207&rot2WorkYn=&templateInfo=&payGbn=&resultCnt=10&keywordJobCont=&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=job&actServExcYn=&keywordStaAreaNm=&maxPay=&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=&resultCntInfo=10&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=&searchOn=Y&subEmpHopeYn=&academicGbn=&foriegn=&templateDepthNoInfo=&mealOfferClcd=&station=&moerButtonYn=&holidayGbn=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=&stationNm=&benefitGbn=&keywordFlag=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=5d8b1778-9610-43c7-b253-f963f887b957&keywordBusiNm=&preferentialGbn=all&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex='+ str(page) +'&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL'
        driver.get(lnk)

        companies = driver.find_elements_by_xpath("//table[@class='board-list']/tbody/tr/td[@class='a-l va-t'][2]/div[@class='cp-info']/div[@class='cp-info-in']/a")
        print(len(companies))

        company_lnks = []
        for company in companies:
            company_lnk = company.get_attribute('href')
            if (len(company_lnk) > 200): # Ajax
                company_lnk = 'https://www.work.go.kr/empInfo/empInfoSrch/detail/retrivePriEmpDtlView.do?searchInfoType=CJK&iorgGbcd=CJK&wantedAuthNo='+ "".join(reversed(company_lnk[-1:-9:-1]))
            print('link : ', len(company_lnk), company_lnk)
            if (len(company_lnk) >= 158 or "".join(reversed(company_lnk[-1:-9:-1])).isdigit()):
                company_lnks.append(company_lnk)

        for company_lnk in company_lnks:
            driver.get(company_lnk)
            if (len(company_lnk) > 130): # Ajax
                company_name = driver.find_element_by_xpath("//div[@class='info']//ul//li//div").text
                company_email = driver.find_element_by_xpath("//td[@pil='PR_EMAIL']").text
            else:
                company_name = driver.find_element_by_xpath("//div[@class='careers-private']/p[@class='name']").text
                company_email = driver.find_element_by_xpath("//div[@class='careers-table charge center no-qr']/table/tbody/tr/td[5]").text
            data = [company_name, company_email]

            if len(data[1]) != 0:
                datas.append(data)
            print(company_name, ' -> ', company_email)

        print('\n')
    mk_csv(datas, './output_worknet.csv')

def crawling_rocketPunch(driver):
    # move to rocketPunch
    driver.get('https://www.rocketpunch.com/jobs?')

    # login
    login_lnk = driver.find_element_by_link_text('로그인').get_attribute('href')
    driver.get(login_lnk)

    ID = 'hsung951027@gmail.com'
    PW = 'hsin0520'

    ID_input = driver.find_element_by_id('id-login-email')
    PW_input = driver.find_element_by_id('id-login-password')

    ID_input.send_keys(ID)
    PW_input.send_keys(PW)

    login_btn = driver.find_element_by_xpath("//button[@type='submit']")
    login_btn.click()

    # add filters
    sw = driver.find_element_by_xpath("//a[@data-caption='SW 개발']"); driver.get(sw.get_attribute('href'))
    hw = driver.find_element_by_xpath("//a[@data-caption='HW 개발']"); driver.get(hw.get_attribute('href'))
    game = driver.find_element_by_xpath("//a[@data-caption='게임 개발']"); driver.get(game.get_attribute('href'))
    pm = driver.find_element_by_xpath("//a[@data-caption='기획/PM']"); driver.get(pm.get_attribute('href'))
    design = driver.find_element_by_xpath("//a[@data-caption='디자인']"); driver.get(design.get_attribute('href'))

    ws = driver.find_element_by_xpath("//a[@data-caption='웹서비스']"); driver.get(ws.get_attribute('href'))
    mb = driver.find_element_by_xpath("//a[@data-caption='모바일']"); driver.get(mb.get_attribute('href'))
    e_commerce = driver.find_element_by_xpath("//a[@data-caption='e-commerce']"); driver.get(e_commerce.get_attribute('href'))
    IoT = driver.find_element_by_xpath("//a[@data-caption='IoT']"); driver.get(IoT.get_attribute('href'))
    O2O = driver.find_element_by_xpath("//a[@data-caption='O2O']"); driver.get(O2O.get_attribute('href'))
    finTech = driver.find_element_by_xpath("//a[@data-caption='핀테크']"); driver.get(finTech.get_attribute('href'))
    e_commerce = driver.find_element_by_xpath("//a[@data-caption='e-commerce']"); driver.get(e_commerce.get_attribute('href'))

    # switch to next page
    pages = driver.find_element_by_xpath("//div[@class='ui pagination menu']//div[@class='tablet computer large screen widescreen only']").find_elements_by_tag_name('a')
    last_page = pages[-1].text

    datas = []
    for page in range(1, int(last_page)+1):
        print('page number : ', page)

        driver.get('https://www.rocketpunch.com/jobs?job=3&job=1&job=10&job=9&job=2&tag=O2O&page='+str(page)+'&tag=%ED%95%80%ED%85%8C%ED%81%AC&tag=%EC%9B%B9%EC%84%9C%EB%B9%84%EC%8A%A4&tag=e-commerce&tag=IoT&tag=%EB%AA%A8%EB%B0%94%EC%9D%BC')
        print(driver.current_url)

        companies = driver.find_elements_by_class_name('company-name')
        company_lnks = []

        # collecting company list in current page
        for company in companies:
            company_lnk = company.find_element_by_tag_name('a').get_attribute('href')
            company_lnks.append(company_lnk)

        # travel each company
        for company_lnk in company_lnks:
            driver.get(company_lnk)
            try:
                company_name  = driver.find_element_by_id('company-name').find_element_by_tag_name('h1').text
                company_email = driver.find_element_by_id('company-email').find_element_by_tag_name('a').text
                print(company_name, ' -> ', company_email)
                data = [company_name, company_email]
            except:
                company_name  = driver.find_element_by_id('company-name').find_element_by_tag_name('h1').text
                print(company_name, 'has No email')
                data = [company_name, '']
            if len(data[1]) != 0:
                datas.append(data)
            # break
        print(datas) # accumulate page's data
        print('\n')
    mk_csv(datas, './output_rocket.csv')

def main():
    driver = initialize_selenium()
    # crawling_rocketPunch(driver)
    crawling_workNet(driver)

if __name__ == "__main__":
	main()