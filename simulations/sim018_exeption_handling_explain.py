# import sys

# try:
#     # --- THE TRY ZONE (The Attempt) ---
#     print("\n--- Initiating Calculation ---")
#     raw_input = input("Enter a number to divide 100 by: ")
    
#     # Potential ValueError: If user types "abc"
#     number = int(raw_input) 
    
#     # Potential ZeroDivisionError: If user types "0"
#     result = 100 / number

# except ValueError:
#     # Triggered if data type conversion fails
#     print("❌ ERROR: Data Type Mismatch. Please enter digits only (0-9).")

# except ZeroDivisionError:
#     # Triggered by the laws of mathematics
#     print("❌ ERROR: Universe Implosion Avoided. You cannot divide by zero.")

# except KeyboardInterrupt:
#     # Triggered if the user presses Ctrl+C to force-quit
#     print("\n⚠️  WARNING: User forced a manual shutdown.")
#     sys.exit() # Cleanly exits the program

# except Exception as e:
#     # The Safety Net for everything else (Network issues, Memory issues, etc.)
#     print(f"❓ UNKNOWN ERROR: An unexpected issue occurred: {e}")

# else:
#     # --- THE ELSE ZONE (The Victory Lap) ---
#     # This ONLY runs if NO errors occurred above.
#     print(f"✅ SUCCESS: Calculation complete!")
#     print(f"The final result is: {result}")

# finally:
#     # --- THE FINALLY ZONE (The Cleanup) ---
#     # This runs no matter what happened before.
#     print("🧹 CLEANUP: Closing all active processes...")
#     print("--- Session Ended ---")