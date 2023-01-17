import json
import os

to_curl = [
"https://api.github.com/users/LingDong-/repos?per_page=100",
"https://api.github.com/orgs/wenyan-lang/repos?per_page=100"
]

hl = [[[z for z in y.split("\n") if len(z)] for y in x.split("--------") if len (y)] for x in open("highlights.txt",'r').read().split("========") if len(x)]

lang_colors = {'1C Enterprise': '814CCC', 'ABAP': 'E8274B', 'ActionScript': '882B0F', 'Ada': '02f88c', 'Agda': '315665', 'AGS Script': 'B9D9FF', 'Alloy': '64C800', 'AMPL': 'E6EFBB', 'AngelScript': 'C7D7DC', 'ANTLR': '9DC3FF', 'API Blueprint': '2ACCA8', 'APL': '5A8164', 'AppleScript': '101F1F', 'Arc': 'aa2afe', 'ASP': '6a40fd', 'AspectJ': 'a957b0', 'Assembly': '6E4C13', 'Asymptote': '4a0c0c', 'ATS': '1ac620', 'AutoHotkey': '6594b9', 'AutoIt': '1C3552', 'Ballerina': 'FF5000', 'Batchfile': 'C1F12E', 'BlitzMax': 'cd6400', 'Boo': 'd4bec1', 'Brainfuck': '2F2530', 'C': '555555', 'C#': '178600', 'C++': 'f34b7d', 'Ceylon': 'dfa535', 'Chapel': '8dc63f', 'Cirru': 'ccccff', 'Clarion': 'db901e', 'Clean': '3F85AF', 'Click': 'E4E6F3', 'Clojure': 'db5855', 'CoffeeScript': '244776', 'ColdFusion': 'ed2cd6', 'Common Lisp': '3fb68b', 'Common Workflow Language': 'B5314C', 'Component Pascal': 'B0CE4E', 'Crystal': '000100', 'CSS': '563d7c', 'Cuda': '3A4E3A', 'D': 'ba595e', 'Dart': '00B4AB', 'DataWeave': '003a52', 'Dhall': 'dfafff', 'DM': '447265', 'Dockerfile': '384d54', 'Dogescript': 'cca760', 'Dylan': '6c616e', 'E': 'ccce35', 'eC': '913960', 'ECL': '8a1267', 'Eiffel': '946d57', 'Elixir': '6e4a7e', 'Elm': '60B5CC', 'Emacs Lisp': 'c065db', 'EmberScript': 'FFF4F3', 'EQ': 'a78649', 'Erlang': 'B83998', 'F#': 'b845fc', 'F*': '572e30', 'Factor': '636746', 'Fancy': '7b9db4', 'Fantom': '14253c', 'Faust': 'c37240', 'FLUX': '88ccff', 'Forth': '341708', 'Fortran': '4d41b1', 'FreeMarker': '0050b2', 'Frege': '00cafe', 'G-code': 'D08CF2', 'Game Maker Language': '71b417', 'GAML': 'FFC766', 'GDScript': '355570', 'Genie': 'fb855d', 'Gherkin': '5B2063', 'Glyph': 'c1ac7f', 'Gnuplot': 'f0a9f0', 'Go': '00ADD8', 'Golo': '88562A', 'Gosu': '82937f', 'Grammatical Framework': '79aa7a', 'Groovy': 'e69f56', 'Hack': '878787', 'Harbour': '0e60e3', 'Haskell': '5e5086', 'Haxe': 'df7900', 'HiveQL': 'dce200', 'HolyC': 'ffefaf', 'HTML': 'e34c26', 'Hy': '7790B2', 'IDL': 'a3522f', 'Idris': 'b30000', 'IGOR Pro': '0000cc', 'Io': 'a9188d', 'Ioke': '078193', 'Isabelle': 'FEFE00', 'J': '9EEDFF', 'Java': 'b07219', 'JavaScript': 'f1e05a', 'Jolie': '843179', 'JSONiq': '40d47e', 'Jsonnet': '0064bd', 'Julia': 'a270ba', 'Jupyter Notebook': 'DA5B0B', 'Kotlin': 'F18E33', 'KRL': '28430A', 'Lasso': '999999', 'Lex': 'DBCA00', 'LFE': '4C3023', 'LiveScript': '499886', 'LLVM': '185619', 'LOLCODE': 'cc9900', 'LookML': '652B81', 'LSL': '3d9970', 'Lua': '000080', 'Makefile': '427819', 'Mask': 'f97732', 'MATLAB': 'e16737', 'Max': 'c4a79c', 'MAXScript': '00a6a6', 'mcfunction': 'E22837', 'Mercury': 'ff2b2b', 'Meson': '007800', 'Metal': '8f14e9', 'Mirah': 'c7a938', 'mIRC Script': '926059', 'MLIR': '5EC8DB', 'Modula-3': '223388', 'MQL4': '62A8D6', 'MQL5': '4A76B8', 'MTML': 'b7e1f4', 'NCL': '28431f', 'Nearley': '990000', 'Nemerle': '3d3c6e', 'nesC': '94B0C7', 'NetLinx': '0aa0ff', 'NetLinx+ERB': '747faa', 'NetLogo': 'ff6375', 'NewLisp': '87AED7', 'Nextflow': '3ac486', 'Nim': '37775b', 'Nit': '009917', 'Nix': '7e7eff', 'Nu': 'c9df40', 'Objective-C': '438eff', 'Objective-C++': '6866fb', 'Objective-J': 'ff0c5a', 'ObjectScript': '424893', 'OCaml': '3be133', 'Odin': '60AFFE', 'Omgrofl': 'cabbff', 'ooc': 'b0b77e', 'Opal': 'f7ede0', 'OpenQASM': 'AA70FF', 'Oxygene': 'cdd0e3', 'Oz': 'fab738', 'P4': '7055b5', 'Pan': 'cc0000', 'Papyrus': '6600cc', 'Parrot': 'f3ca0a', 'Pascal': 'E3F171', 'Pawn': 'dbb284', 'Pep8': 'C76F5B', 'Perl': '0298c3', 'PHP': '4F5D95', 'PigLatin': 'fcd7de', 'Pike': '005390', 'PLSQL': 'dad8d8', 'PogoScript': 'd80074', 'PostScript': 'da291c', 'PowerBuilder': '8f0f8d', 'PowerShell': '012456', 'Processing': '0096D8', 'Prolog': '74283c', 'Propeller Spin': '7fa2a7', 'Puppet': '302B6D', 'PureBasic': '5a6986', 'PureScript': '1D222D', 'Python': '3572A5', 'q': '0040cd', 'QML': '44a51c', 'Quake': '882233', 'R': '198CE7', 'Racket': '3c5caa', 'Ragel': '9d5200', 'Raku': '0000fb', 'RAML': '77d9fb', 'Rascal': 'fffaa0', 'Reason': 'ff5847', 'Rebol': '358a5b', 'Red': 'f50000', "Ren'Py": 'ff7f7f', 'Ring': '2D54CB', 'Riot': 'A71E49', 'Roff': 'ecdebe', 'Rouge': 'cc0088', 'Ruby': '701516', 'RUNOFF': '665a4e', 'Rust': 'dea584', 'SaltStack': '646464', 'SAS': 'B34936', 'Scala': 'c22d40', 'Scheme': '1e4aec', 'sed': '64b970', 'Self': '0579aa', 'Shell': '89e051', 'Shen': '120F14', 'Slash': '007eff', 'Slice': '003fa2', 'Smalltalk': '596706', 'SmPL': 'c94949', 'Solidity': 'AA6746', 'SourcePawn': '5c7611', 'SQF': '3F3F3F', 'Squirrel': '800000', 'SRecode Template': '348a34', 'Stan': 'b2011d', 'Standard ML': 'dc566d', 'Starlark': '76d275', 'SuperCollider': '46390b', 'Swift': 'ffac45', 'SystemVerilog': 'DAE1C2', 'Tcl': 'e4cc98', 'Terra': '00004c', 'TeX': '3D6117', 'TI Program': 'A0AA87', 'Turing': 'cf142b', 'TypeScript': '2b7489', 'UnrealScript': 'a54c4d', 'V': '5d87bd', 'Vala': 'fbe5cd', 'VBA': '867db1', 'VBScript': '15dcdc', 'VCL': '148AA8', 'Verilog': 'b2b7f8', 'VHDL': 'adb2cb', 'Vim script': '199f4b', 'Visual Basic .NET': '945db7', 'Volt': '1F1F1F', 'Vue': '2c3e50', 'wdl': '42f1f4', 'WebAssembly': '04133b', 'wisp': '7582D1', 'Wollok': 'a23738', 'X10': '4B6BEF', 'xBase': '403a40', 'XC': '99DA07', 'XQuery': '5232e7', 'XSLT': 'EB8CEB', 'Yacc': '4B6C4B', 'YARA': '220000', 'YASnippet': '32AB90', 'ZAP': '0d665e', 'ZenScript': '00BCD1', 'Zephir': '118f9e', 'Zig': 'ec915c', 'ZIL': 'dc75e5'}

def read_curl(f):
	j = json.loads(open(f).read())
	print(j)
	return {x['name']:x for x in j}


projs = {}

for tc in to_curl:
	os.system('curl "'+tc+'" > curled.txt')
	projs.update(read_curl("curled.txt"))


out = '<img src="https://github.com/LingDong-/shan-shui-inf/raw/master/screenshots/screen002.jpg?raw=true"></img><table><tr>'

out += """
"""

for i in range(len(hl)):
	topic = hl[i]

	out += '<td valign="top">'
	head = topic[0][0]
	subt = topic[0][1]
	cont = topic[1]

	out += "<h2>"+head+"</h2>"
	out += "<i>"+subt+"</i><br><br>"
	
	for item in cont:
		star = str(projs[item]['stargazers_count'])
		fork = str(projs[item]['forks_count'])
		desc = projs[item]['description']
		lang = projs[item]['language']
		link = projs[item]['html_url']

		cpl = 45
		cc = 0
		desc = desc.split(" ")
		descnl = ""
		for d in desc:
			descnl += d+" "
			cc += len(d)+1
			if cc > cpl:
				descnl += "<br>"
				cc = 0

		out += '<table><tr><td><h3><a href=\"'+link+"\">"+item+"</a></h3>"+descnl+"<br>"+("_"*60)+"</tr><tr><td><img src=\"https://via.placeholder.com/12/"+lang_colors[lang]+"/000000?text=+\"></img>&nbsp;"+lang+"&nbsp;&nbsp;&nbsp;&nbsp;★ "+star+"</td></tr></table>"

	out += "</td>"
	if i % 2 == 1 and i != len(hl)-1:
		out += "</tr><tr>"
out += "</tr></table>"

out += """

The list above is a small selection of my favorite projects. There're a lot more on the [Repos](https://github.com/LingDong-?tab=repositories) page. Check out my [portfolio](https://lingdong.works) and my [Glitch](https://glitch.com/@LingDong-) too!


<sub>This README is generated with a Python script and Github Actions. [How it works](https://github.com/LingDong-/LingDong-/blob/master/generate.py)</sub>


"""

open("README.md",'w').write(out)
