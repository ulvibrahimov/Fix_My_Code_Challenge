# Sort integer arguments (ascending)

result = []
ARGV.each do |arg|
    # Skip if not integer
    next if arg !~ /^-?[0-9]+$/
    
    i_arg = arg.to_i
    
    # Insert i_arg at the right position
    is_inserted = false
    i = 0
    l = result.length
    while !is_inserted && i < l do
        if result[i] > i_arg
            result.insert(i, i_arg)
            is_inserted = true
        end
        i += 1
    end
    result << i_arg if !is_inserted
end

puts result
