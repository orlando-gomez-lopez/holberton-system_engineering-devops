#!/usr/bin/env ruby

if ARGV.length == 1
    for a in ARGV[0].split do
        if ( a =~ /hb{0,1}tn/ )
            print a
        end	
    end
puts "\n"
end
