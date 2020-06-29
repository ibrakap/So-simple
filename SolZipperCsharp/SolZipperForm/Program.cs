using System;
using System.Windows.Forms;
using SolZipperCsharp;

namespace SolZipperForm
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {

            if (args.Length > 0)
            {
                if (args[0] == "pack")
                {
                    SolZipper solZipper = new SolZipper();
                    bool bRes = solZipper.IsThereAnySlnFile(args[1]); 
                    //    = solZipper.ZipIt(args[1]);

                    if (bRes == false)
                    {
                        MessageBox.Show("There is no solution file", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        return;
                    }
                    string sRes = solZipper.ZipIt(args[1]);
                    if (sRes == solZipper.SUCCESS)
                    {
                        MessageBox.Show("Zipped successfully", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    else
                    {
                        MessageBox.Show(sRes, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
                /*
                else if (args[0] == "unpack")
                {

                }
                */
            }
            else
            {
                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new Form1());
            }
        }
    }
}
