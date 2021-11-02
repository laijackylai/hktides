import pandas

fname = './tidal sample data/SWAN/hkb_hsign_nest_20210803.000000.tbl'
col = ['Hsig',     'Hswell',     'Dir',     'X-Windv',     'Y-Windv',      'PkDir',      'Period',     'DrPT01',     'DrPT02',     'DrPT03',     'DrPT04',
       'DrPT05',      'DrPT06',   'TpPT01',     'TpPT02',      'TpPT03',   'TpPT04',    'TpPT05',    'TpPT06',       'HsPT01',   'HsPT02',       'HsPT03', 'HsPT04',   'HsPT05',    'HsPT06']
data = pandas.read_table(
    fname, comment='%', delim_whitespace=True, names=col, header=0)

print(data)

# reference: https://svnserv.csiro.au/svn/EMS/src/main/ext/swan/src/swanmain.ftn
