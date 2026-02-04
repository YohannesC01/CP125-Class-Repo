def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):
    """
    Manages a music playlist with adds, imports, and removals.
    
    Args:
        current_playlist: Set of currently in playlist
        add_songs: List of songs to add individually
        import_playlist: Set of songs to import from Spotify
        banned_songs: Set of songs to remove
    
    Returns:
        int: Count of final songs in playlist
    """
    add_songs_set = set(add_songs)

    for i in add_songs_set:
        current_playlist.add(i)

    all_playlist = current_playlist | import_playlist
    unbanned_song = all_playlist - banned_songs
    while len(unbanned_song) > 6:
        unbanned_song.pop()
    
    return len(unbanned_song)