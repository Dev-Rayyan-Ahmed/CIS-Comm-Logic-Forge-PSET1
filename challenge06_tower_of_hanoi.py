def tower_of_hanoi(no_of_disk: int, source_rod: str, dest_rod: str, aux_rod: str):
    if no_of_disk <= 1:
        print(f"Move Disk {no_of_disk} from {source_rod} to {dest_rod}")
        return
        
    tower_of_hanoi(no_of_disk - 1, source_rod, aux_rod, dest_rod)
    
    print(f"Move Disk {no_of_disk} from {source_rod} to {dest_rod}")
    
    tower_of_hanoi(no_of_disk - 1, aux_rod, dest_rod, source_rod)

tower_of_hanoi(3,'A','C','B')