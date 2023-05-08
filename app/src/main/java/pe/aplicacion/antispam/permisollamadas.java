package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class permisollamadas extends AppCompatActivity {
    TextView txtContinuar, txtNoContinuar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_permisollamadas);

        txtContinuar=findViewById(R.id.textViewPllamadas);
        txtNoContinuar=findViewById(R.id.textViewNoPllamadas);

        txtNoContinuar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Continuar();
            }

            private void Continuar() {
                Intent i = new Intent(permisollamadas.this, permisocontactos.class);
                startActivity(i);
            }
        });

        txtNoContinuar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NoContinuar();
            }

            private void NoContinuar() {

                Intent i = new Intent(permisollamadas.this, ListaPermisos.class);
                startActivity(i);

            }
        });
    }

}