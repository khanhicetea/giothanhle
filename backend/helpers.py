from datetime import datetime, time


def renderMassTimesToString(masses):
    data = [dict(dow=m.day_of_week, time=m.time.strftime('%H.%M')) for m in masses.all()]
    sorted_data = sorted(data, key=lambda k: k['dow']) 
    times = ['{}:{}'.format(m['dow'], m['time']) for m in sorted_data]
    return "\n".join(times)


def parseMassTimes(content):
    rows = [s.strip() for s in content.split("\n") if s.strip()]
    data = []
    for row in rows:
        p = row.split(':')
        if len(p[0]) == 1:
            p[0] += '-' + p[0]
        w = p[0].split('-')
        for x in range(int(w[0]), int(w[1]) + 1):
            dt = datetime.strptime(p[1], '%H.%M')
            data.append(dict(
                day_of_week=x,
                time=dt.time()
            ))
    return data