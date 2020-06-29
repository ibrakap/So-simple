using System;
using System.Drawing;
using System.Windows.Forms;
using SolZipperCsharp;
using SolZipperForm.Properties;

namespace SolZipperForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public SolZipper solZipper = new SolZipper();
        protected override void OnLoad(EventArgs e)
        {
            this.Visible = false;
            this.Opacity = 1;
            Win32import.AnimateWindow(this.Handle, 1000, Win32import.AnimateWindowFlags.AW_HOR_NEGATIVE);
            button1.Image = SystemIcons.Information.ToBitmap();
            base.OnLoad(e);
        }
        private void InstallButton_Click(object sender, EventArgs e)
        {
            solZipper.InstallFile(Application.ExecutablePath);
            string ReturnCode = solZipper.InstallRegisterExtension(solZipper.ContextMenuSelection);
            if (ReturnCode == solZipper.SUCCESS)
            {
                MessageBox.Show("Succesfully installed!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else if (ReturnCode == solZipper.ALREADYINSTALLED)
            {
                MessageBox.Show("Already installed!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                MessageBox.Show("Error occured\n " + ReturnCode, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void UninstallButton_Click(object sender, EventArgs e)
        {
            solZipper.UninstallFile();
            string ReturnCode = solZipper.UninstallRegisterExtension();
            if (ReturnCode == solZipper.SUCCESS)
            {
                MessageBox.Show("Succesfully uninstalled!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Error occured\n" + ReturnCode, "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void Selection1_CheckedChanged(object sender, EventArgs e)
        {
            if (Selection1.Checked == true)
            {
                solZipper.ContextMenuSelection = solZipper.CASCADED_CONTEXT_MENU;
            }
        }

        private void Selection2_CheckedChanged(object sender, EventArgs e)
        {
            if (Selection2.Checked == true)
            {
                solZipper.ContextMenuSelection = solZipper.NORMAL_CONTEXT_MENU;
            }
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Inspired Rake's SolZipper", "Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void Form1_Load_1(object sender, EventArgs e)
        {
            button1.Image = SystemIcons.Information.ToBitmap();
        }
    }
}
