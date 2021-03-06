import urllib2
import re
from bs4 import BeautifulSoup
import smtplib  

opener= urllib2.build_opener()
opener.addheaders = [('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
#Part 1


#Run this, then comment out this code and run code at bottom to find what links are dead.
outToFile = open('pagenotfound1.txt', mode='w')
outToFile.write('')
outToFile.close()

def extractlinks(blspage):
    url = (blspage)

    ourUrl = opener.open(url).read()

    soup = BeautifulSoup(ourUrl)

    sets = soup.find_all('a',class_='external')

    outToFile = open('pagenotfound.txt', mode='w')
    outToFile.write(str(sets))
    outToFile.close()
    

    f = open('pagenotfound.txt')

    strToSearch = ""

    for line in f:
        strToSearch += line

    #print(strToSearch)

    #compile method says what regular expression you want to search for
    patFinder1 = re.compile('href=".*?"')
    patFinder2 = re.compile('href="')
    patFinder3 = re.compile('"')
    

    findPat1 = re.search(patFinder1, strToSearch)

    #.group prints what was found
    try:
        #print(findPat1.group())
        findPat1 = re.findall(patFinder1, strToSearch)
        
        outToFile = open('pagenotfound1.txt', mode='a+')
        outToFile.write(url+'\n')
        for i in findPat1:
            subFound = patFinder2.sub('', i)
            subFound2 = patFinder3.sub('', subFound)
            print(subFound2)
            outToFile.write(subFound2+'\n')
        
        outToFile.close()
    
        
    

    except AttributeError:
        print "errors"
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/aerospace-engineering-and-operations-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/aerospace-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/agricultural-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/architects.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/biomedical-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/cartographers-and-photogrammetrists.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/chemical-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/civil-engineering-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/civil-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/computer-hardware-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/drafters.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/electrical-and-electronics-engineering-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/electrical-and-electronics-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/electro-mechanical-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/environmental-engineering-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/environmental-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/health-and-safety-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/industrial-engineering-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/industrial-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/landscape-architects.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/marine-engineers-and-naval-architects.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/materials-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/mechanical-engineering-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/mechanical-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/mining-and-geological-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/nuclear-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/petroleum-engineers.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/surveying-and-mapping-technicians.htm')
extractlinks('http://www.bls.gov/ooh/architecture-and-engineering/print/surveyors.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/art-directors.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/craft-and-fine-artists.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/fashion-designers.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/floral-designers.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/graphic-designers.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/industrial-designers.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/interior-designers.htm')
extractlinks('http://www.bls.gov/ooh/arts-and-design/print/multimedia-artists-and-animators.htm')
extractlinks('http://www.bls.gov/ooh/building-and-grounds-cleaning/print/grounds-maintenance-workers.htm')
extractlinks('http://www.bls.gov/ooh/building-and-grounds-cleaning/print/janitors-and-building-cleaners.htm')
extractlinks('http://www.bls.gov/ooh/building-and-grounds-cleaning/print/maids-and-housekeeping-cleaners.htm')
extractlinks('http://www.bls.gov/ooh/building-and-grounds-cleaning/print/pest-control-workers.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/accountants-and-auditors.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/appraisers-and-assessors-of-real-estate.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/budget-analysts.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/claims-adjusters-appraisers-examiners-and-investigators.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/compensation-benefits-and-job-analysis-specialists.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/cost-estimators.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/financial-analysts.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/financial-examiners.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/fundraisers.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/human-resources-specialists-and-labor-relations-specialists.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/insurance-underwriters.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/loan-officers.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/logisticians.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/management-analysts.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/market-research-analysts.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/meeting-convention-and-event-planners.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/personal-financial-advisors.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/purchasing-managers-buyers-and-purchasing-agents.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/tax-examiners-and-collectors-and-revenue-agents.htm')
extractlinks('http://www.bls.gov/ooh/business-and-financial/print/training-and-development-specialists.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/health-educators.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/mental-health-counselors-and-marriage-and-family-therapists.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/probation-officers-and-correctional-treatment-specialists.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/rehabilitation-counselors.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/school-and-career-counselors.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/social-and-human-service-assistants.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/social-workers.htm')
extractlinks('http://www.bls.gov/ooh/community-and-social-service/print/substance-abuse-and-behavioral-disorder-counselors.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/computer-and-information-research-scientists.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/computer-network-architects.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/computer-programmers.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/computer-support-specialists.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/computer-systems-analysts.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/database-administrators.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/information-security-analysts.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/network-and-computer-systems-administrators.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/software-developers.htm')
extractlinks('http://www.bls.gov/ooh/computer-and-information-technology/print/web-developers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/boilermakers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/brickmasons-blockmasons-and-stonemasons.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/carpenters.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/cement-mason-and-terrazzo-workers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/construction-and-building-inspectors.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/construction-equipment-operators.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/construction-laborers-and-helpers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/drywall-and-ceiling-tile-installers-and-tapers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/electricians.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/elevator-installers-and-repairers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/glaziers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/hazardous-materials-removal-workers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/insulation-workers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/painters-construction-and-maintenance.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/plumbers-pipefitters-and-steamfitters.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/roofers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/sheet-metal-workers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/solar-photovoltaic-installers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/structural-iron-and-steel-workers.htm')
extractlinks('http://www.bls.gov/ooh/construction-and-extraction/print/tile-and-marble-setters.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/adult-literacy-and-ged-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/curators-museum-technicians-and-conservators.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/career-and-technical-education-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/high-school-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/instructional-coordinators.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/kindergarten-and-elementary-school-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/librarians.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/library-technicians-and-assistants.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/middle-school-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/postsecondary-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/preschool-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/special-education-teachers.htm')
extractlinks('http://www.bls.gov/ooh/education-training-and-library/print/teacher-assistants.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/actors.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/athletes-and-sports-competitors.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/coaches-and-scouts.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/dancers-and-choreographers.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/music-directors-and-composers.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/musicians-and-singers.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/producers-and-directors.htm')
extractlinks('http://www.bls.gov/ooh/entertainment-and-sports/print/umpires-referees-and-other-sports-officials.htm')
extractlinks('http://www.bls.gov/ooh/farming-fishing-and-forestry/print/agricultural-workers.htm')
extractlinks('http://www.bls.gov/ooh/farming-fishing-and-forestry/print/fishers-and-related-fishing-workers.htm')
extractlinks('http://www.bls.gov/ooh/farming-fishing-and-forestry/print/forest-and-conservation-workers.htm')
extractlinks('http://www.bls.gov/ooh/farming-fishing-and-forestry/print/logging-workers.htm')
extractlinks('http://www.bls.gov/ooh/food-preparation-and-serving/print/bartenders.htm')
extractlinks('http://www.bls.gov/ooh/food-preparation-and-serving/print/chefs-and-head-cooks.htm')
extractlinks('http://www.bls.gov/ooh/food-preparation-and-serving/print/cooks.htm')
extractlinks('http://www.bls.gov/ooh/food-preparation-and-serving/print/food-and-beverage-serving-and-related-workers.htm')
extractlinks('http://www.bls.gov/ooh/food-preparation-and-serving/print/food-preparation-workers.htm')
extractlinks('http://www.bls.gov/ooh/food-preparation-and-serving/print/waiters-and-waitresses.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/athletic-trainers-and-exercise-physiologists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/audiologists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/chiropractors.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/dental-assistants.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/dental-hygienists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/dentists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/diagnostic-medical-sonographers.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/dietitians-and-nutritionists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/emts-and-paramedics.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/genetic-counselors.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/home-health-aides.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/licensed-practical-and-licensed-vocational-nurses.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/massage-therapists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/medical-and-clinical-laboratory-technologists-and-technicians.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/medical-assistants.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/medical-records-and-health-information-technicians.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/medical-transcriptionists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/nuclear-medicine-technologists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/nurse-anesthetists-nurse-midwives-and-nurse-practitioners.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/nursing-assistants.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/occupational-health-and-safety-specialists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/occupational-health-and-safety-technicians.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/occupational-therapists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/occupational-therapy-assistants-and-aides.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/opticians-dispensing.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/optometrists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/orthotists-and-prosthetists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/personal-care-aides.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/pharmacists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/pharmacy-technicians.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/phlebotomists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/physical-therapist-assistants-and-aides.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/physical-therapists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/physician-assistants.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/physicians-and-surgeons.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/podiatrists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/psychiatric-technicians-and-aides.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/radiation-therapists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/radiologic-technologists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/recreational-therapists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/registered-nurses.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/respiratory-therapists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/speech-language-pathologists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/surgical-technologists.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/veterinarians.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/veterinary-assistants-and-laboratory-animal-caretakers.htm')
extractlinks('http://www.bls.gov/ooh/healthcare/print/veterinary-technologists-and-technicians.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/aircraft-and-avionics-equipment-mechanics-and-technicians.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/automotive-body-and-glass-repairers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/automotive-service-technicians-and-mechanics.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/computer-atm-and-office-machine-repairers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/diesel-service-technicians-and-mechanics.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/electrical-and-electronics-installers-and-repairers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/general-maintenance-and-repair-workers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/heating-air-conditioning-and-refrigeration-mechanics-and-installers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/heavy-vehicle-and-mobile-equipment-service-technicians.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/industrial-machinery-mechanics-and-maintenance-workers-and-millwrights.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/line-installers-and-repairers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/medical-equipment-repairers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/small-engine-mechanics.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/telecommunications-equipment-installers-and-repairers-except-line-installers.htm')
extractlinks('http://www.bls.gov/ooh/installation-maintenance-and-repair/print/wind-turbine-technicians.htm')
extractlinks('http://www.bls.gov/ooh/legal/print/arbitrators-mediators-and-conciliators.htm')
extractlinks('http://www.bls.gov/ooh/legal/print/court-reporters.htm')
extractlinks('http://www.bls.gov/ooh/legal/print/judges-and-hearing-officers.htm')
extractlinks('http://www.bls.gov/ooh/legal/print/lawyers.htm')
extractlinks('http://www.bls.gov/ooh/legal/print/paralegals-and-legal-assistants.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/agricultural-and-food-science-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/agricultural-and-food-scientists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/anthropologists-and-archeologists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/atmospheric-scientists-including-meteorologists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/biochemists-and-biophysicists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/biological-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/chemical-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/chemists-and-materials-scientists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/conservation-scientists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/economists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/environmental-science-and-protection-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/environmental-scientists-and-specialists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/epidemiologists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/forensic-science-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/forest-and-conservation-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/geographers.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/geological-and-petroleum-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/geoscientists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/historians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/hydrologists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/medical-scientists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/microbiologists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/nuclear-technicians.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/physicists-and-astronomers.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/political-scientists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/psychologists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/sociologists.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/survey-researchers.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/urban-and-regional-planners.htm')
extractlinks('http://www.bls.gov/ooh/life-physical-and-social-science/print/zoologists-and-wildlife-biologists.htm')
extractlinks('http://www.bls.gov/ooh/management/print/administrative-services-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/advertising-promotions-and-marketing-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/architectural-and-engineering-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/compensation-and-benefits-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/computer-and-information-systems-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/construction-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/elementary-middle-and-high-school-principals.htm')
extractlinks('http://www.bls.gov/ooh/management/print/emergency-management-directors.htm')
extractlinks('http://www.bls.gov/ooh/management/print/farmers-ranchers-and-other-agricultural-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/financial-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/food-service-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/human-resources-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/industrial-production-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/lodging-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/medical-and-health-services-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/natural-sciences-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/postsecondary-education-administrators.htm')
extractlinks('http://www.bls.gov/ooh/management/print/preschool-and-childcare-center-directors.htm')
extractlinks('http://www.bls.gov/ooh/management/print/property-real-estate-and-community-association-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/public-relations-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/sales-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/social-and-community-service-managers.htm')
extractlinks('http://www.bls.gov/ooh/management/print/top-executives.htm')
extractlinks('http://www.bls.gov/ooh/management/print/training-and-development-managers.htm')
extractlinks('http://www.bls.gov/ooh/math/print/actuaries.htm')
extractlinks('http://www.bls.gov/ooh/math/print/mathematicians.htm')
extractlinks('http://www.bls.gov/ooh/math/print/operations-research-analysts.htm')
extractlinks('http://www.bls.gov/ooh/math/print/statisticians.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/announcers.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/broadcast-and-sound-engineering-technicians.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/editors.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/film-and-video-editors-and-camera-operators.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/interpreters-and-translators.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/photographers.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/public-relations-specialists.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/reporters-correspondents-and-broadcast-news-analysts.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/technical-writers.htm')
extractlinks('http://www.bls.gov/ooh/media-and-communication/print/writers-and-authors.htm')
extractlinks('http://www.bls.gov/ooh/military/print/military-careers.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/bill-and-account-collectors.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/bookkeeping-accounting-and-auditing-clerks.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/customer-service-representatives.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/desktop-publishers.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/financial-clerks.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/general-office-clerks.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/information-clerks.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/material-recording-clerks.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/police-fire-and-ambulance-dispatchers.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/postal-service-workers.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/receptionists.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/secretaries-and-administrative-assistants.htm')
extractlinks('http://www.bls.gov/ooh/office-and-administrative-support/print/tellers.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/animal-care-and-service-workers.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/barbers-hairdressers-and-cosmetologists.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/childcare-workers.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/fitness-trainers-and-instructors.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/funeral-service-occupations.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/gaming-services-occupations.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/manicurists-and-pedicurists.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/recreation-workers.htm')
extractlinks('http://www.bls.gov/ooh/personal-care-and-service/print/skincare-specialists.htm')
extractlinks('http://www.bls.gov/ooh/production/print/assemblers-and-fabricators.htm')
extractlinks('http://www.bls.gov/ooh/production/print/bakers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/butchers-and-meat-cutters.htm')
extractlinks('http://www.bls.gov/ooh/production/print/dental-and-ophthalmic-laboratory-technicians-and-medical-appliance-technicians.htm')
extractlinks('http://www.bls.gov/ooh/production/print/food-and-tobacco-processing-workers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/jewelers-and-precious-stone-and-metal-workers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/laundry-and-dry-cleaning-workers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/machinists-and-tool-and-die-makers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/metal-and-plastic-machine-workers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/painting-and-coating-workers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/power-plant-operators-distributors-and-dispatchers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/printing-workers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/quality-control-inspectors.htm')
extractlinks('http://www.bls.gov/ooh/production/print/semiconductor-processors.htm')
extractlinks('http://www.bls.gov/ooh/production/print/slaughterers-meat-packers-and-meat-poultry-and-fish-cutters-and-trimmers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/stationary-engineers-and-boiler-operators.htm')
extractlinks('http://www.bls.gov/ooh/production/print/water-and-wastewater-treatment-plant-and-system-operators.htm')
extractlinks('http://www.bls.gov/ooh/production/print/welders-cutters-solderers-and-brazers.htm')
extractlinks('http://www.bls.gov/ooh/production/print/woodworkers.htm')
extractlinks('http://www.bls.gov/ooh/protective-service/print/correctional-officers.htm')
extractlinks('http://www.bls.gov/ooh/protective-service/print/firefighters.htm')
extractlinks('http://www.bls.gov/ooh/protective-service/print/fire-inspectors-and-investigators.htm')
extractlinks('http://www.bls.gov/ooh/protective-service/print/police-and-detectives.htm')
extractlinks('http://www.bls.gov/ooh/protective-service/print/private-detectives-and-investigators.htm')
extractlinks('http://www.bls.gov/ooh/protective-service/print/security-guards.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/advertising-sales-agents.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/cashiers.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/insurance-sales-agents.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/models.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/real-estate-brokers-and-sales-agents.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/retail-sales-workers.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/sales-engineers.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/securities-commodities-and-financial-services-sales-agents.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/travel-agents.htm')
extractlinks('http://www.bls.gov/ooh/sales/print/wholesale-and-manufacturing-sales-representatives.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/airline-and-commercial-pilots.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/air-traffic-controllers.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/bus-drivers.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/delivery-truck-drivers-and-driver-sales-workers.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/flight-attendants.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/hand-laborers-and-material-movers.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/heavy-and-tractor-trailer-truck-drivers.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/material-moving-machine-operators.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/railroad-occupations.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/taxi-drivers-and-chauffeurs.htm')
extractlinks('http://www.bls.gov/ooh/transportation-and-material-moving/print/water-transportation-occupations.htm')

#Part 2
'''

f = open('pagenotfound1.txt')

for line in f:
    url=line
    #print url
    try:    
        ourUrl = opener.open(url).read()
        patFinder1 = re.compile('Page Not Found')
        findPat1 = re.search(patFinder1, ourUrl)
        
        
    
        findPat1 = re.findall(patFinder1, ourUrl) 
        
        for i in findPat1:
            print url
            print(i)
        
        
        
        
    except urllib2.HTTPError, e:
        print url
        print e.code

    except urllib2.URLError, e:
        print e.args

    except Exception as e:
        print e

'''

