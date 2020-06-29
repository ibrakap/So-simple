using System;
using System.IO;
using System.IO.Compression;
using Microsoft.Win32;

namespace SolZipperCsharp
{
    public class SolZipper
    {
        // Gets %appdata% folder and adds SolZipper string inorder to create installation folder path string
        private static readonly string InstallationFolder = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData).ToString(), "SolZipper");
        // Name difference, variable name changed for easy to read
        private readonly string UninstallationFolder = InstallationFolder;
        // Adds Temp string inorder to create Temp folder path string
        private readonly string TempFolder = Path.Combine(InstallationFolder, @"Temp");
        // Bad Files or Folder what we want to delete, now readonly infuture it will be costumizeable
        private readonly string[] BadFilesOrFolders = { "Release", "Debug", "Browse.VC.db", "ipch", ".pdb", ".git" };

        // Return Values
        public readonly string SUCCESS = "SUCCESS";
        public readonly string UNKNOWN = "UNKNOWN";
        public readonly string ALREADYREMOVED = "ALREADYREMOVED";
        public readonly string ALREADYINSTALLED = "ALREADYINSTALLED";
        // End of return values

        // public value for context menu selection
        public int ContextMenuSelection;
        // End of public setable values 

        // Context menu options
        public readonly int CASCADED_CONTEXT_MENU = 0;
        public readonly int NORMAL_CONTEXT_MENU = 1;
        // End of context menu options

        // Installs application. If function success it return SUCCESS otherwise it returns Exception name
        public string InstallFile(string ApplicationPath)
        {
            /* ApplicationPath paramter takes your application path
             * inorder to give application path you can use Application.ExecutablePath in form project, 
             * if you are using Console application you can give Assembly.GetExecutingAssembly().CodeBase.Replace("file:///", "");
             */
            if (!(Directory.Exists(InstallationFolder)))
            {
                Directory.CreateDirectory(InstallationFolder);
                try
                {
                    File.Copy(ApplicationPath, InstallationFolder + "\\SolZipper.exe", true);
                }
                catch (Exception e)
                {
                    return e.GetType().Name;
                }
            }
            return SUCCESS;
        }
        // Installs register extension of application. If function success it returns SUCCESS, if extension already installed it returns ALREADYINSTALLED, otherwise it returns Exception name
        public string InstallRegisterExtension(int InstallationType)
        {
            /* 
            InstallationType paramater could take two int 0 and 1
            if InstallationType is 0 it installs Cascade menu, if InstallationType is 1 it installs normal context menu
            */
            string RegSetString = "\"" + InstallationFolder + "\\SolZipper.exe\"" + " " + "\"pack\"" + " " + "\"%1\"";
            RegistryKey CheckKey = Registry.LocalMachine.OpenSubKey(@"SOFTWARE\Classes\Folder\shell\");
            foreach (string iterator in CheckKey.GetSubKeyNames())
            {
                if (iterator == "SolZipper")
                {
                    return ALREADYINSTALLED;
                }
            }
            try
            {
                if (InstallationType == CASCADED_CONTEXT_MENU)
                {
                    RegistryKey RegKey = Registry.LocalMachine.OpenSubKey(@"SOFTWARE\Classes\Folder\shell\", true);
                    RegistryKey SolZipper = RegKey.CreateSubKey("SolZipper", true);
                    SolZipper.SetValue("subcommands", "");
                    RegistryKey shellKey = SolZipper.CreateSubKey("shell");
                    RegistryKey zipKey = shellKey.CreateSubKey("Zip Solution");
                    RegistryKey comKey = zipKey.CreateSubKey("command");
                    comKey.SetValue("", RegSetString);
                }
                else if (InstallationType == NORMAL_CONTEXT_MENU)
                {
                    RegistryKey RegKey = Registry.LocalMachine.OpenSubKey(@"SOFTWARE\Classes\Folder\shell\", true);
                    RegistryKey SolZipper = RegKey.CreateSubKey("SolZipper", true);
                    SolZipper.SetValue("", "Zip it with SolZipper");
                    RegistryKey comKey = SolZipper.CreateSubKey("command");
                    comKey.SetValue("", RegSetString);
                }
                else
                {
                    return UNKNOWN;
                }
            }
            catch (Exception e)
            {
                return e.GetType().Name;
            }
            return SUCCESS;
        }
        // Takes Solution Folder path and process zip operation 
        public string ZipIt(string Dir)
        {
            string DirName = new DirectoryInfo(Dir).Name;
            string Tmp = TempFolder + "\\" + DirName;

            if (!(Directory.Exists(TempFolder)))
            {
                Directory.CreateDirectory(TempFolder);
            }
            DirectoryCopy(Dir, Tmp);
            FilterFiles(Tmp);
            if (File.Exists(Dir[1] + ".zip"))
            {
                File.Delete(Dir[1] + ".zip");
            }
            try
            {
                ZipFile.CreateFromDirectory(Tmp, Dir+ ".zip", CompressionLevel.Fastest, true);
            }
            catch (Exception e)
            {
                return e.GetType().Name;
            }
            // Delete remains
            Directory.Delete(Tmp, true);
            return SUCCESS;
        }
        public string UninstallFile()
        {
            if (Directory.Exists(UninstallationFolder))
            {
                Directory.Delete(UninstallationFolder, true);
                return SUCCESS;
            }
            return ALREADYREMOVED;

        }
        // Removes register extension if operation success it return SUCCESS otherwise returns Exception name
        public string UninstallRegisterExtension()
        {
            try
            {
                RegistryKey CheckKey = Registry.LocalMachine.OpenSubKey(@"SOFTWARE\Classes\Folder\shell\", true);
                CheckKey.DeleteSubKeyTree("SolZipper", true);
            }
            catch (Exception e)
            {
                return e.GetType().Name;
            }
            return SUCCESS;
        }
        // Gets Files from folders and subfolders, returns string array
        private string[] GetRecursiveDirectoryList(string Dir)
        {
            return Directory.GetFileSystemEntries(Dir, "*", SearchOption.AllDirectories);
        }
        // Another function taken from stackoverflow, Copies directory with subfolders
        private void DirectoryCopy(string source, string destination)
        {
            DirectoryInfo dir = new DirectoryInfo(source);
            DirectoryInfo[] dirs = dir.GetDirectories();

            if (!Directory.Exists(destination))
            {
                Directory.CreateDirectory(destination);
            }

            FileInfo[] files = dir.GetFiles();

            foreach (FileInfo file in files)
            {
                string temppath = Path.Combine(destination, file.Name);
                file.CopyTo(temppath, true);
            }

            foreach (DirectoryInfo subdir in dirs)
            {
                string temppath = Path.Combine(destination, subdir.Name);
                DirectoryCopy(subdir.FullName, temppath);
            }
        }
        // Controls Visual Studio Solution File (".sln") in folder, if folder contains solution file it returns true otherwise false
        public bool IsThereAnySlnFile(string sourcedir)
        {
            string[] RdirList = GetRecursiveDirectoryList(sourcedir);
            foreach (string i in RdirList)
            {
                if (i.EndsWith(".sln"))
                {
                    return true;
                }
            }
            return false;
        }
        private string FilterFiles(string Dir)
        {
            string[] keep = GetRecursiveDirectoryList(Dir);
            foreach (string i in keep)
            {
                if (File.Exists(i))
                {
                    var fi = new FileInfo(i);
                    fi.Attributes = FileAttributes.Normal;
                }
                foreach (string ci in BadFilesOrFolders)
                {
                    if (i.EndsWith(ci))
                    {
                        if (File.Exists(i))
                        {
                            FileInfo fi = new FileInfo(i);
                            fi.Attributes |= FileAttributes.Normal;
                            fi.Delete();
                        }
                        else if (Directory.Exists(i))
                        {
                            var di = new DirectoryInfo(i);
                            try
                            {
                                di.Delete(true);
                            }
                            catch (Exception e)
                            {
                                DeleteReadOnlyDirectory(i);
                            }
                        }
                    }
                }
                keep = GetRecursiveDirectoryList(Dir);
            }
            return SUCCESS;
        }
        private void DeleteReadOnlyDirectory(string directory)
        {
            foreach (var subdirectory in Directory.EnumerateDirectories(directory))
            {
                DeleteReadOnlyDirectory(subdirectory);
            }
            foreach (var fileName in Directory.EnumerateFiles(directory))
            {
                var fileInfo = new FileInfo(fileName);
                fileInfo.Attributes = FileAttributes.Normal;
                fileInfo.Delete();
            }
            Directory.Delete(directory);
        }
    }
}
