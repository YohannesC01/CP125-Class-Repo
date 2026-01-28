def synchronize_databases(legacy_list, modern_set, blacklist):
    legacy_id = set()
    blacklist_set = set(blacklist)
    
    for id,email in legacy_list:
        if email not in blacklist_set:
            legacy_id.add(id)

    lost_set = legacy_id - modern_set

    ghost_set = modern_set - legacy_id

    return(lost_set,ghost_set)
 
