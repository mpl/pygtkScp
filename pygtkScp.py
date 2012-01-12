import gtk

def browseCallBack(self, widget, data=None):
	print "Hello again - %s was pressed" % data
	browse()

def browse():
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
		print dialog.get_filename(), 'selected'
	elif response == gtk.RESPONSE_CANCEL:
		print 'Closed, no files selected'
	dialog.destroy()

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

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	mainWindow()
	main()

