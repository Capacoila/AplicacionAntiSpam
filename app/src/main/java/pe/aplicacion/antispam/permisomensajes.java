package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class permisomensajes extends AppCompatActivity {
    TextView txtContinuarPMensajes, txtNoContinuarPMensajes;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_permisomensajes);

        txtContinuarPMensajes=findViewById(R.id.textViewPMensajes);
        txtNoContinuarPMensajes=findViewById(R.id.textViewNoPMensajes);

        txtNoContinuarPMensajes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Continuar();
            }

            private void Continuar() {
                Intent i = new Intent(permisomensajes.this, PedirNumero.class);
                startActivity(i);
            }
        });

        txtNoContinuarPMensajes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NoContinuar();
            }

            private void NoContinuar() {

                Intent i = new Intent(permisomensajes.this, permisomensajes.class);
                startActivity(i);

            }
        });
    }
}