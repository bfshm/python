f = open('10-2.html', 'w')

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
f.write('<table border="1">')
f.write('<tr><th>Name</th><th>Score</th><tr>')
f.write('\n'.join(tds))
f.write('</table>')

f.close()