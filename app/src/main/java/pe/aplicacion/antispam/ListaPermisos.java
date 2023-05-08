package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class ListaPermisos extends AppCompatActivity {
    TextView txtContinuar, txtNoContinuar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lista_permisos);

        txtContinuar=findViewById(R.id.textviewContinuar);
        txtNoContinuar=findViewById(R.id.textviewCancelar);

        txtNoContinuar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Continuar();
            }

            private void Continuar() {
                Intent i = new Intent(ListaPermisos.this, permisollamadas.class);
                startActivity(i);
            }
        });

        txtNoContinuar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NoContinuar();
            }

            private void NoContinuar() {

                Intent i = new Intent(ListaPermisos.this, BlockPredeterminada.class);
                startActivity(i);

            }
        });
    }
}