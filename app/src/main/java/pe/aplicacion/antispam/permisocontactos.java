package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class permisocontactos extends AppCompatActivity {
    TextView txtContinuarPContactos, txtNoContinuarPContactos;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_permisocontactos);
        txtContinuarPContactos=findViewById(R.id.textViewPContactos);
        txtNoContinuarPContactos=findViewById(R.id.textViewNoPContactos);

        txtNoContinuarPContactos.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Continuar();
            }

            private void Continuar() {
                Intent i = new Intent(permisocontactos.this, permisomensajes.class);
                startActivity(i);
            }
        });

        txtNoContinuarPContactos.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NoContinuar();
            }

            private void NoContinuar() {

                Intent i = new Intent(permisocontactos.this, permisollamadas.class);
                startActivity(i);

            }
        });
    }
}