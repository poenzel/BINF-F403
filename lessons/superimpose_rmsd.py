
from pymol import cmd

def superimpose_and_compute_rmsd():
    
    # Get the list of all objects in the PyMOL session
    objects = cmd.get_object_list()
        
    # Align all structures to the first one in the list using the main chain atoms
    reference = objects[0]
    print(f"Using {reference} as the reference structure for superimposition.")
    
    for obj in objects[1:]:
        cmd.align(f"{obj} and name CA", f"{reference} and name CA")  # Align using alpha carbons (Cα)
    
    # Compute RMSD for all pairs
    rmsd_results = {}
    for i, obj1 in enumerate(objects):
        for j, obj2 in enumerate(objects):
            if i < j:
                # Measure RMSD between main chains
                rmsd = cmd.rms_cur(
                    f"{obj1} and name CA",  # First selection
                    f"{obj2} and name CA"   # Second selection
                )
                rmsd_results[(obj1, obj2)] = rmsd
    
    # Print RMSD results
    print("RMSD between structures:")
    for (obj1, obj2), rmsd in rmsd_results.items():
        print(f"RMSD({obj1}, {obj2}) = {rmsd:.3f} Å")

# To run the function in PyMOL, call:
# superimpose_and_compute_rmsd()
