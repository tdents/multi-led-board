use Purple;
$device="/dev/led-monitor";

###
%PLUGIN_INFO = (
	perl_api_version => 2,
	name => "LED-Monitor",
	version => "1.0",
	summary => "LED-Monitor",
	description => "LED-board control plugin for pidgin",
	author => "Kenshi",
	url => "http://localhost/",
	load => "plugin_load",
	unload => "plugin_unload"
);

sub plugin_init {
	Purple::Debug::info("FlashyLightPlugin", "LEDPlugin init: $device\n");
        open(OUTPUT,">",$device);
        print OUTPUT "1,0\n";
        close OUTPUT;

	return %PLUGIN_INFO;
}
sub on {
	Purple::Debug::info("FlashyLightPlugin", "LEDPlugin on device: $device\n");
	open(OUTPUT,">",$device);
	print OUTPUT "1,1\n";
	close OUTPUT;
}

sub off {
	Purple::Debug::info("FlashyLightPlugin", "LEDPlugin off device: $device\n");
        open(OUTPUT,">", "/dev/led-monitor");
        print OUTPUT "1,0\n";
        close OUTPUT;
}

sub plugin_load {
	plugin_init();
        my $plugin = shift;
	my $conv_handle = Purple::Conversations::get_handle();
	
	Purple::Signal::connect($conv_handle, "received-im-msg", $plugin, \&update_unread_count, '');
	Purple::Signal::connect($conv_handle, "received-chat-msg", $plugin, \&update_unread_count, '');
	Purple::Signal::connect($conv_handle, "conversation-updated", $plugin, \&update_unread_count, '');
	Purple::Signal::connect($conv_handle, "conversation-created", $plugin, \&update_unread_count, '');
	Purple::Signal::connect($conv_handle, "deleting-conversation", $plugin, \&update_unread_count, '');
	
}

sub total_unread_count {
	my $total_unread = 0;
	my @convs = Purple::get_conversations();

	for my $conv (@convs) {
		my $data = $conv->get_data('unseen-count');
		next unless defined($data);
		my $this_unread = $data->{_purple};
		$total_unread += $this_unread;
	}
	return $total_unread;
}

sub update_unread_count {
	$count=0;
	my $unread = total_unread_count();
	if ($unread > 0) { on() }
	else { off() }
}

sub plugin_unload {
	off();
	my $plugin = shift;
}
