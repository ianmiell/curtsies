from __future__ import unicode_literals
import pexpect
import curtsies
from curtsies.fmtfuncs import blue, red, green 

def main(command):

	pexpect_session = pexpect.spawn(command)
	with curtsies.FullscreenWindow() as window:
		while True:
			a = curtsies.FSArray(window.height,window.width)
			text = 'pexpect window manager ' + str(window.height) + 'x' + str(window.width)
			a[0:1,0:len(text)] = [blue(text)]
			window.render_to_terminal(a)
			try:
				res=pexpect_session.read_nonblocking(timeout=1)
			except pexpect.EOF:
				pass
			
if __name__ == '__main__':
	main('ls')
