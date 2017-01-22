#include <gtk/gtk.h>
#include <string>
#include <sstream>
using namespace std;
 
GtkWidget *g_lbl_print_epoch;

int main(int argc, char *argv[])
{
    GtkBuilder      *builder; 
    GtkWidget       *window;
 
    gtk_init(&argc, &argv);
 
    builder = gtk_builder_new();
    gtk_builder_add_from_file (builder, "glade/window_main.glade", NULL);
 
    window = GTK_WIDGET(gtk_builder_get_object(builder, "window_main"));
    
    gtk_builder_connect_signals(builder, NULL);
    g_lbl_print_epoch = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_print_epoch"));
    g_object_unref(builder);
 
    gtk_widget_show(window);                
    gtk_main();
    gtk_label_set_text(GTK_LABEL(g_lbl_print_epoch), "click");
    return 0;
}


void on_get_epoch_clicked()
{   
       const gchar *epoch[30] = {0};
    stringstream prepoch;
    
    time_t result = time(NULL);
    if(result != -1) 
     {

    result << prepoch;
{
    const std::string& tmp = prepoch.str();   
    *epoch = tmp.c_str();
    }
    return;

    
     }
    
gtk_label_set_text(GTK_LABEL(g_lbl_print_epoch), *epoch);
    
}

// called when window is closed
void on_window_main_destroy()
{
    gtk_main_quit();
}


