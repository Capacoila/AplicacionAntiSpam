package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class BlockPredeterminada extends AppCompatActivity {

    TextView txtPermitir, txtNoPermitir;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_blockpredeterminada);

        txtPermitir=findViewById(R.id.txtPermitir);
        txtNoPermitir=findViewById(R.id.txtNoPermitir);

        txtPermitir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Permitir();
            }

            private void Permitir() {
                Intent i = new Intent(BlockPredeterminada.this, ListaPermisos.class);
                startActivity(i);
            }
        });

        txtNoPermitir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NoPermitir();
            }

            private void NoPermitir() {

                Intent i = new Intent(BlockPredeterminada.this, Comenzar.class);
                startActivity(i);

            }
        });
    }
}
