#!/usr/bin/env ruby

if ARGV.length == 1
    if ARGV[0].length == 10
        if ( ARGV[0] =~ /\d\d\d\d\d\d\d\d\d\d/ )
            print ARGV[0]
        end	
    end
puts "\n"
end
