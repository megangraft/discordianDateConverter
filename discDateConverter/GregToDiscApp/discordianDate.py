import datetime

def discordianDate(ymd):
    year_ordinal = ymd.toordinal() - datetime.date(ymd.year, 1, 1).toordinal() + 1
    disc_yold = int(ymd.year) + 1166
    if ymd.year % 4 == 0:
        if ymd == datetime.date(ymd.year, 2, 29):
            return "No weekday, between the 59th and 60th day of Chaos in the YOLD " + str(disc_yold) + ". Celebrate St. Tib\'s Day!"
    year_days = datetime.date(ymd.year, 12, 31).toordinal() - datetime.date(ymd.year, 1, 1).toordinal() + 1
    weekdays = {1:"Sweetmorn", 2:"Boomtime", 3:"Pungenday", 4:"Prickle-Prickle", 0:"Setting Orange"}
    seasons = {range(1,74):"Chaos",
                  range(74,147):"Discord",
                  range(147,220):"Confusion",
                  range(220,293):"Bureaucracy",
                  range(293,366):"The Aftermath"}
    holidays = {"5Chaos":"Mungday", "50Chaos":"Chaoflux",
                   "5Discord":"Mojoday", "50Discord":"Discoflux",
                   "5Confusion":"Syaday", "50Confusion":"Confuflux",
                   "5Bureaucracy":"Zaraday", "50Bureaucracy":"Bureflux",
                   "5The Aftermath":"Maladay", "50The Aftermath":"Afflux"}
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    if year_days == 366:
        year_days = 365
        if year_ordinal > 60:
            year_ordinal -= 1
    disc_weekday = weekdays.get(year_ordinal%5)
    disc_season = {seasons[key] for key in seasons if year_ordinal in key}.pop()
    disc_season_day = year_ordinal%73 if year_ordinal%73>0 else 73
    disc_date = disc_weekday + ", the " + ordinal(disc_season_day) + " day of " + disc_season + " in the YOLD " + str(disc_yold)
    if disc_season_day == 5 or disc_season_day == 50:
        disc_holiday = holidays.get(str(disc_season_day)+disc_season)
        return disc_date + ". Celebrate " + disc_holiday + "!"
    return disc_date
