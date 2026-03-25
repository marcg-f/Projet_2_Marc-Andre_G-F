import icalendar
import datetime
import message
ajd = datetime.date.today()
ajd = str(ajd)
ajd = ajd.replace("-", "")
print(ajd)
message.next_col()
fichier = "calendrier_collecte.ics"
with open(fichier, 'r') as file:
    for line_no, line in enumerate(file, start=1):
        debut = line.split(":")
        if(debut[0] == "DTSTART"):
            time = debut[1].split("T")
            date = time[0]
            if(date >= ajd):
                bac_info = line[2+line_no].split(":")
                bac_nom = bac_info[0]
        deuxieme = line[13+line_no]
        deuxieme = line.split(":")
        if(deuxieme[0] == "DTSTART"):
            time = deuxieme[1].split("T")
            date_2 = time[0]
            if(date_2 == date):
                bac_info_2 = line[15+line_no].split(":")
                bac_nom_2 = bac_info_2[0]

