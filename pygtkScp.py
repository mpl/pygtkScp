import gtk
import os

def browse(self, entry=None):
	print 'file: ', entry.get_text()
	dialog = gtk.FileChooserDialog("Open..",
		None,
		gtk.FILE_CHOOSER_ACTION_OPEN,
		(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
		gtk.STOCK_OPEN, gtk.RESPONSE_OK))
	dialog.set_default_response(gtk.RESPONSE_OK)

	filter = gtk.FileFilter()
	filter.set_name("All files")
	filter.add_pattern("*")
	dialog.add_filter(filter)

	response = dialog.run()
	if response == gtk.RESPONSE_OK:
		entry.set_text(dialog.get_filename())
	elif response == gtk.RESPONSE_CANCEL:
		print 'Closed, no files selected'
	dialog.destroy()

def doScp(self, source, destination):
	src = source.get_text()
	dest = destination.get_text()
	args = ['scp']
	if os.path.isdir(src):
		args.append('-r')
	args.append(src)
	args.append(dest)
	os.execv("/usr/bin/scp", args)
	
# abject oriented is for wusses, hence do it all in one func like a boss
def doAll():
	# Create a new window
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)

	window.set_title("Scp")

	# It's a good idea to do this for all windows.
	window.connect("destroy", lambda wid: gtk.main_quit())
	window.connect("delete_event", lambda a1,a2:gtk.main_quit())

	# Sets the border width of the window.
	window.set_border_width(10)

	# This calls our box creating function
	box0 = gtk.VBox(False, 0)
	box0.set_border_width(2)

	sBox = gtk.HBox(False, 0)
	sBox.set_border_width(2)
	label1 = gtk.Label("Browse")
	button1 = gtk.Button()
	button1.add(label1)
	entry1 = gtk.Entry()
	entry1.set_text("enter source or browse")
	button1.connect("clicked", browse, entry1)
	usEntry = gtk.Entry()
	usEntry.set_text("username")
	psEntry = gtk.Entry()
	psEntry.set_text("password")
	sBox.pack_start(entry1, False, False, 3)
	sBox.pack_start(button1, False, False, 3)
	entry1.show()
	label1.show()
	button1.show()

	dBox = gtk.HBox(False, 0)
	dBox.set_border_width(2)
	label2 = gtk.Label("Browse")
	button2 = gtk.Button()
	button2.add(label2)
	entry2 = gtk.Entry()
	entry2.set_text("enter dest or browse")
	button2.connect("clicked", browse, entry2)
	udEntry = gtk.Entry()
	udEntry.set_text("username")
	pdEntry = gtk.Entry()
	pdEntry.set_text("password")
	dBox.pack_start(entry2, False, False, 3)
	dBox.pack_start(button2, False, False, 3)
	entry2.show()
	label2.show()
	button2.show()

	actionBox = gtk.HBox(False, 0)
	actionBox.set_border_width(2)
	label3 = gtk.Label("Engage")
	button3 = gtk.Button()
	button3.add(label3)
	button3.connect("clicked", doScp, entry1, entry2)
	actionBox.pack_start(button3, False, False, 3)
	label3.show()
	button3.show()

	box0.pack_start(sBox, False, False, 3)
	box0.pack_start(dBox, False, False, 3)
	box0.pack_start(actionBox, False, False, 3)
	sBox.show()
	dBox.show()
	actionBox.show()
	box0.show()

	window.add(box0)
	window.show()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	doAll()
	main()

