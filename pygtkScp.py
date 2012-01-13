import gtk
import os

def browseCallBack(self, entry=None):
	browse(entry)
	print 'file: ', entry.get_text()

def browse(entry):
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

	filter = gtk.FileFilter()
	filter.set_name("Images")
	filter.add_mime_type("image/png")
	filter.add_mime_type("image/jpeg")
	filter.add_mime_type("image/gif")
	filter.add_pattern("*.png")
	filter.add_pattern("*.jpg")
	filter.add_pattern("*.gif")
	filter.add_pattern("*.tif")
	filter.add_pattern("*.xpm")
	dialog.add_filter(filter)

	response = dialog.run()
	if response == gtk.RESPONSE_OK:
#		print dialog.get_filename(), 'selected'
		data = dialog.get_filename()
		entry.set_text(data)
	elif response == gtk.RESPONSE_CANCEL:
		print 'Closed, no files selected'
		data = ''
	dialog.destroy()
	return data

def sourceBox():
	sBox = gtk.HBox(False, 0)
	sBox.set_border_width(2)

	label1 = gtk.Label("Browse")
	button1 = gtk.Button()
	button1.add(label1)
	button1.connect("clicked", browseCallBack, "cool button")

	entry = gtk.Entry()

	sBox.pack_start(entry, False, False, 3)
	sBox.pack_start(button1, False, False, 3)
	entry.show()
	label1.show()
	button1.show()

	return sBox

def mainBox():
	box0 = gtk.HBox(False, 0)
	box0.set_border_width(2)

	sBox = sourceBox()
	dBox = sourceBox()

	box0.pack_start(sBox, False, False, 3)
	box0.pack_start(dBox, False, False, 3)
	sBox.show()
	dBox.show()

	return box0

def mainWindow():
	# Create a new window
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)

	window.set_title("Scp")

	# It's a good idea to do this for all windows.
	window.connect("destroy", lambda wid: gtk.main_quit())
	window.connect("delete_event", lambda a1,a2:gtk.main_quit())

	# Sets the border width of the window.
	window.set_border_width(10)

	# This calls our box creating function
	box0 = mainBox()
	box0.show()

	window.add(box0)
	window.show()

def doScp(self, source, dest):
#	try:
	os.execl("/usr/bin/scp", "scp", source.get_text(), dest.get_text())
#	except OSError:
#		print "nope"
	
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
	button1.connect("clicked", browseCallBack, entry1)
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
	button2.connect("clicked", browseCallBack, entry2)
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

