#!/usr/bin/env ruby
list = []
if ARGV.length == 1
    for a in ARGV[0].split do
        list.push(a)
    end
    for b in list do
        for c in 0.. b.length do
            if b[c] =~ /[A-Z]/
	        print b[c]
	    end	
	end
    end
puts "\n"
end
