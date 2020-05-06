#!/usr/bin/ruby

rgb = ARGV.map { |x| (x.to_f * 255).round.to_s(16) }
puts('#' + rgb.join('').upcase)