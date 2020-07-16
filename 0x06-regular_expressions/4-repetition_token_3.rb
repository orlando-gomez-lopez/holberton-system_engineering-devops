#!/usr/bin/env ruby

if ARGV.length == 1
    for a in ARGV[0].split do
        if ( a =~ /hbt{0,10}n/ )
            print a
        end	
    end
puts "\n"
end
