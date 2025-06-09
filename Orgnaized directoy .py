import os
import shutil


def organize_files(directory):
    try:
        files = os.listdir(directory)

        
        files = [file for file in files if os.path.isfile(os.path.join(directory, file))]

        if not files:
            print("❗ No files found in the directory.")
            return
        
       
        for file in files:
            # Get the file extension (e.g., '.txt', '.jpg')
            file_extension = file.split('.')[-1].lower()
            
            
            if len(file.split('.')) == 1:
                continue
 
            folder_name = f"{file_extension}_files"
            folder_path = os.path.join(directory, folder_name)

            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                print(f"✅ Created folder: {folder_name}")

            
            src = os.path.join(directory, file)
            dest = os.path.join(folder_path, file)
            shutil.move(src, dest)
            print(f"✅ Moved file: {file} to {folder_name}")

        print("\nAll files have been organized successfully!")

    except Exception as e:
        print(f"❗ Error: {e}")


def main():
    directory = input("Enter the path of the directory to organize: ").strip()

  
    if not os.path.isdir(directory):
        print("❗ The directory does not exist.")
    else:
        organize_files(directory)

if __name__ == "__main__":
    main()
